import asyncio
import pytest


async def HandleConnection(reader, writer):
    request = None
    while request != 'quit':
        try:
            request = (await reader.read(255)).decode('utf8')
            if not request:
                break
            print(f"REQUEST: {request}")
            writer.write(request.encode('utf8'))
            await writer.drain()
        except Exception as e:
            print("ERROR in HandleConnection:", e)
    print("About to close writer")
    writer.close()
    print("Writer closed")


async def main():
    server = await asyncio.start_server(HandleConnection, '0.0.0.0', 15555)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')
    async with server:
        await server.serve_forever()
        # await server.start_serving()


@pytest.mark.asyncio
async def test_server():
    print("Creating server task..")
    server_task = asyncio.create_task(main())
    await asyncio.sleep(100)
    try:
        server_task.cancel(msg="CANCELL THE SERVER")
    except asyncio.CancelledError as e:
        print("ASYNC CANCELLED ERROR:", e)
    print(f"SERVER STATUS: {server_task.cancelled()}")



if __name__ == '__main__':
    # https://docs.python.org/3/library/asyncio-task.html#task-cancellation
    # asyncio.run(main())
    asyncio.run(test_server())