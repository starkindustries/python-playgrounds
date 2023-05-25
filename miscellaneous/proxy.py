import socket
import threading

# Set the proxy server IP and port
proxy_server_ip = '0.0.0.0'
proxy_server_port = 12345

# Set the target server IP and port
target_server_ip = 'your_target_ip'
target_server_port = 80

def handle_client(client_socket):
    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_socket.connect((target_server_ip, target_server_port))

    # Forward data from client to target server
    def forward_to_target():
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            target_socket.send(data)
        client_socket.close()
        target_socket.close()

    # Forward data from target server to client
    def forward_to_client():
        while True:
            data = target_socket.recv(4096)
            if not data:
                break
            client_socket.send(data)
        client_socket.close()
        target_socket.close()

    # Start threads to forward data
    threading.Thread(target=forward_to_target).start()
    threading.Thread(target=forward_to_client).start()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((proxy_server_ip, proxy_server_port))
    server.listen(5)
    print(f"[*] Listening on {proxy_server_ip}:{proxy_server_port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Received incoming connection from {addr[0]}:{addr[1]}")

        # Handle the incoming connection in a new thread
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    main()
