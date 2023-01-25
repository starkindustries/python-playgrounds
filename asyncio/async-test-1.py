import asyncio

async def download(data):
    if data in ['b', 'c']:
        1/0    # simulate error
    return 42  # success

async def coro(data_list):
    coroutines = [download(data) for data in data_list]
    return await asyncio.gather(*coroutines, return_exceptions=True)

async def main():
    task1 = asyncio.create_task(coro(["a", "b", "c"]))
    task2 = asyncio.create_task(coro(["d", "e", "f"]))
    return await asyncio.gather(task1, task2, return_exceptions=True)

result = asyncio.run(main())
print(result)
for responses in result:
    for response in responses:
        if isinstance(response, Exception):
            print("Exception:", response)
        else:
            print("Success:", response)