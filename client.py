import socket
import threading
import sys

def receive_messages(client_socket):
    try:
        while True:
            response = client_socket.recv(1024)
            if response:
                print(f"Received from server: {response.decode()}")
            else:
                print("Server closed the connection.")
                break
    except Exception as e:
        print(f"Error receiving messages: {e}")
    finally:
        client_socket.close()
        sys.exit()

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('127.0.0.1', 5055))
        print("Connected to server.")

        # Start a thread to receive messages from the server
        threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

        while True:
            message = input("I am from client: ")
            client_socket.sendall(message.encode())
    except KeyboardInterrupt:
        print("Client shutting down...")
    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
