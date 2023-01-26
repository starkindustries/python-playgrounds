import asyncio

async def coro2():
    await asyncio.sleep(10)
    print("CORO 2 SUCCESS!")
    return "coro2 success!"

async def divide_by_zero():
    return 1/0    # simulate error    

async def square_number(n):
    for i in range(1,n+1):
        print("Square of ",i, "is ", i**2)
        await asyncio.sleep(0.001)

async def square_root(n):
    print("Square root of ",n," rounded to nearest integer is ",
        round(n**.5))


async def main():
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(square_number(5))
        task_group.create_task(square_root(25))
        task_group.create_task(coro2())
        task_group.create_task(square_root(18))
        task_group.create_task(divide_by_zero())
    print("All different tasks of task_group has executed successfully!!")

async def main2():
    task1 = asyncio.create_task(square_number(5))
    task2 = asyncio.create_task(square_root(25))
    task3 = asyncio.create_task(coro2())    
    task4 = asyncio.create_task(square_root(18))
    task5 = asyncio.create_task(divide_by_zero())
    # r1 = await task1
    # if any([isinstance(item, Exception) for item in r1]):
    #     print("Exception:", r1)
    # r2 = await task2
    # return [r1, r2]
    return await asyncio.gather(task1, task2, task3, task4, task5, return_exceptions=False)

responses = asyncio.run(main())
print("RESPONSES", responses)
