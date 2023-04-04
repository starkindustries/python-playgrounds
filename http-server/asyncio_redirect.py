import asyncio

async def handle_request(reader, writer):
    data = await reader.read(4096)
    print(f"data({len(data)}): [{data}]")
    request_line = data.decode().split('\r\n')[0]
    request_method, path, _ = request_line.split(' ')

    if request_method in ('GET', 'POST', 'PUT', 'DELETE', 'HEAD'):
        # Change the redirect location as needed
        redirect_location = 'https://example.com/'

        response = f'HTTP/1.1 301 Moved Permanently\r\n'
        response += f'Location: {redirect_location}\r\n'
        response += '\r\n'

        writer.write(response.encode())
        await writer.drain()

    writer.close()

async def main():
    server = await asyncio.start_server(handle_request, '0.0.0.0', 8000)

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped.")
