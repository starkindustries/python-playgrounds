import asyncio

async def download(data):
    if data in ['b', 'c']:
        1/0    # simulate error
    #return 42  # success

async def coro(data_list):
    coroutines = [download(data) for data in data_list]
    return await asyncio.gather(*coroutines, return_exceptions=True)


async def coro2():
    await asyncio.sleep(10)
    return "coro2 success!"

async def coro3():
    await asyncio.sleep(1)
    return "coro3 success!"


async def main1():
    task1 = asyncio.create_task(coro(["a", "b", "c"]))
    #task2 = asyncio.create_task(coro(["d", "e", "f"]))
    task2 = asyncio.create_task(coro2())
    r1 = await task1
    if any([isinstance(item, Exception) for item in r1]):
        print("Exception:", r1)
    r2 = await task2
    return [r1, r2]
    # return await asyncio.gather(task1, task2, return_exceptions=True)


async def main2():
    task1 = asyncio.create_task(coro(['a', 'b', 'c']))
    task2 = asyncio.create_task(coro3())
    task3 = asyncio.create_task(coro3())    
    task4 = asyncio.create_task(coro2())
    task5 = asyncio.create_task(download('b'))
    # r1 = await task1
    # if any([isinstance(item, Exception) for item in r1]):
    #     print("Exception:", r1)
    # r2 = await task2
    # return [r1, r2]
    return await asyncio.gather(task1, task2, task3, task4, task5, return_exceptions=False)



result = asyncio.run(main2())
print(result)
for responses in result:
    if not responses:
        continue
    if isinstance(responses, str):
        print(responses)
        continue
    if hasattr(responses, "__len__"):
        for response in responses:
            if isinstance(response, Exception):
                print("Exception:", response)
            else:
                print("Success:", response)