import asyncio


async def download(data):
    if data in ['b', 'c']:
        1/0    # simulate error
    return 42  # success


async def async_test2(data1, data2):
        print("Entering PtySession.WriteTaskEntry()")
        result = 0
        try:
            result += await asyncio.wait_for(download(data1), timeout=1.0)
            result += await download(data2)
        except TimeoutError:
            pass

        except asyncio.exceptions.TimeoutError:
            pass

        except ConnectionResetError:
            print("Connection reset.")

        print("Leaving PtySession.WriteTaskEntry()")
        return result




async def coro(data_list):
    coroutines = [download(data) for data in data_list]
    return await asyncio.gather(*coroutines, return_exceptions=True)

async def main():
    task1 = asyncio.create_task(async_test2("d", "e"))
    task2 = asyncio.create_task(async_test2("a", "b"))
    # this returns error: Task exception was never retrieved
    # https://stackoverflow.com/questions/65147823/python-asyncio-task-exception-was-never-retrieved 
    # try:
    #     await task1
    #     await task2
    # except Exception as e:
    #     print(f"ERROR: {e}")
    results = await asyncio.gather(task1, task2, return_exceptions=True)
    print(results)
    for result in results:
        if isinstance(result, Exception):
            print(f"CAUGHT EXCEPTION: {result}")
        else:
            print(f"FOUND RESULT: {result}")

asyncio.run(main())