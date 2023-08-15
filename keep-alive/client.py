import socket
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 12345)
print(f'Connecting to {server_address[0]} port {server_address[1]}')
sock.connect(server_address)

try:
    # Send some data
    message = 'This is a test message.'
    print(f'Sending: {message}')
    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f'Received: {data.decode()}')

finally:
    print('Closing socket')
    sock.close()
