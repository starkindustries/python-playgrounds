import asyncio

# Define the proxy server's address and port
PROXY_ADDRESS = '127.0.0.1'
PROXY_PORT = 7777

# Define the target server's address and port
TARGET_ADDRESS = 'example.com'
TARGET_PORT = 80

async def test_proxy():
    # Connect to the proxy server
    reader, writer = await asyncio.open_connection(PROXY_ADDRESS, PROXY_PORT)
    print("checkpoint")

    # Prepare the request to send to the target server
    # user_input = ""
    # while user_input != "quit":
    # request = f"GET / HTTP/1.1\r\nHost: {TARGET_ADDRESS}:{TARGET_PORT}\r\nConnection: close\r\n\r\n"
    
    request = "helloworld"    
    print(f"writing request: {request}")
    writer.write(request.encode())
    print("Request sent!")

    # Read the response from the target server
    response = await reader.read(4096)
    print("Response from the target server:")
    print(response.decode())

    # Close the connection to the proxy server
    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    asyncio.run(test_proxy())
