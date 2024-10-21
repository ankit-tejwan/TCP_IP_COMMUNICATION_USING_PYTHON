import socket
import threading

def handle_client(connection, client_address):
    print(f"Successfully Client connected: {client_address}")
    try:
        while True:
            data = connection.recv(1024)
            if data:
                print(f"Received from client: {data.decode()}")
                connection.sendall(data)  # Echo back the data
            else:
                break
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        print(f"Client disconnected: {client_address}")
        connection.close()

def start_server(host='127.0.0.1', port=5055):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    # server_socket.bind(('127.0.0.1', 5005))
    server_socket.listen()
    print("Waiting for a connection...")

    try:
        while True:
            connection, client_address = server_socket.accept()
            threading.Thread(target=handle_client, args=(connection, client_address)).start()
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
