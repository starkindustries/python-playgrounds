import asyncio
import time
import sys

async def send_hello(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    for i in range(100):
        message_plus_num = message + str(i)
        print(f'Sending: {message_plus_num}')
        writer.write(message_plus_num.encode())

        data = await reader.read(100)
        print(f'Received: {data.decode()}')

        time.sleep(1)

    print('Closing the connection')
    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    assert len(sys.argv) > 1
    asyncio.run(send_hello(sys.argv[1]))
