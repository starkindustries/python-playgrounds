import asyncio


async def download(data):
    if data in ['b', 'c']:
        1/0    # simulate error
    return 42  # success


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')
    
    async with server:
        asyncio.gather()
        await server.serve_forever()


async def test_server():
    
    print("Creating server task..")
    server_task = asyncio.create_task(main())
    download_task = asyncio.create_task(download('b'))
    
    # await asyncio.sleep(10)    
    # server_task.cancel()
    
    try:
        await download_task
        await server_task
    except asyncio.CancelledError:
        print("server_task cancelled")
    # print(f"SERVER STATUS: {server_task.cancelled()}")
    print("Test completed")


if __name__ == '__main__':
    # https://docs.python.org/3/library/asyncio-task.html#task-cancellation
    asyncio.run(test_server())