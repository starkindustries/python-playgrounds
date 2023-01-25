#!/usr/bin/env python3

# https://realpython.com/async-io-python/
# countasync.py

import asyncio

async def count(id):
    print(id, ": One")
    await asyncio.sleep(1)
    print(id, ": Two")

async def main():
    await count("a")
    await count("b")
    await count("c")
    print("BREAK")
    await asyncio.gather(count("a"), count("b"), count("c"))

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


# https://docs.python.org/3/library/asyncio-eventloop.html
# async def client_connected(reader, writer):
#     # Communicate with the client with
#     # reader/writer streams.  For example:
#     await reader.readline()

# async def main(host, port):
#     srv = await asyncio.start_server(client_connected, host, port)
#     await srv.serve_forever()

# asyncio.run(main('127.0.0.1', 0))