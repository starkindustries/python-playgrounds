import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enable TCP keepalive
sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

# Optional: After 1 second of idleness, start sending keepalive packets every 1 second
if hasattr(socket, 'TCP_KEEPIDLE') and hasattr(socket, 'TCP_KEEPINTVL'):
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 1)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 1)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    connection, client_address = sock.accept()

    try:
        print('Connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('Received {!r}'.format(data))
            if data:
                print('Sending data back to the client...')
                connection.sendall(data)
            else:
                print('No data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
