import asyncio
import socket

# Define the target server's address and port
TARGET_ADDRESS = '127.0.0.1'
TARGET_PORT = 8000

# Define the proxy server's address and port
PROXY_ADDRESS = '127.0.0.1'
PROXY_PORT = 7777

async def forward_data(reader, writer):
    try:
        while not reader.at_eof():            
            data = await reader.read(4096)
            print(f"Forwarding data: {data}")
            if len(data) == 0:
                break
            writer.write(data)
            await writer.drain()
    except Exception as e:
        print(f"ERROR: forwarding data: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

async def handle_client(client_reader, client_writer):
    target_reader, target_writer = await asyncio.open_connection(TARGET_ADDRESS, TARGET_PORT)
    print(f"target connection opened! {TARGET_ADDRESS}:{TARGET_PORT}")

    # Forward data between client and target server
    client_to_target = asyncio.create_task(forward_data(client_reader, target_writer))
    target_to_client = asyncio.create_task(forward_data(target_reader, client_writer))

    await asyncio.gather(client_to_target, target_to_client)


async def start_proxy_server():
    server = await asyncio.start_server(handle_client, PROXY_ADDRESS, PROXY_PORT)
    print(f"[*] Listening on {PROXY_ADDRESS}:{PROXY_PORT}")

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(start_proxy_server())