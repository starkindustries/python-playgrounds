import asyncio

# Define the target server's address and port
TARGET_ADDRESS = '0.0.0.0'
TARGET_PORT = 50000

async def handle_request(reader, writer):
    # Read the incoming request
    request = await reader.read(4096)
    print("Received request:")
    print(request.decode())

    # Prepare a simple HTTP response
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        "Connection: close\r\n"
        "\r\n"
        "<html><body><h1>Hello from the target server!</h1></body></html>"
    )    

    # Send the response back to the client
    writer.write(response.encode())
    await writer.drain()

    # Close the connection
    writer.close()
    await writer.wait_closed()

async def start_target_server():
    server = await asyncio.start_server(handle_request, TARGET_ADDRESS, TARGET_PORT)
    print(f"[*] Target server listening on {TARGET_ADDRESS}:{TARGET_PORT}")

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(start_target_server())
