# servlet.py
import socket

def handle_client(client_socket):
    data = client_socket.recv(1024).decode('utf-8')
    return data

def start():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip_address, 9999))
    server_socket.listen(1)  # Only accept one connection

    print("Server started. Waiting for connections...")

    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address[0]}:{client_address[1]}")

    return client_socket
def main():
  client_socket = start()
  handle_client(client_socket)

if __name__ == "__main__":
  main()