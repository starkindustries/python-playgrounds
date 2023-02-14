import asyncio

 

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
        task_group.create_task(server_coroutine())
        task_group.create_task(square_root(18))
        task_group.create_task(divide_by_zero())
    print("All different tasks of task_group has executed successfully!!")

async def main2():
    task1 = asyncio.create_task(square_number(5))
    task2 = asyncio.create_task(square_root(25))
    task3 = asyncio.create_task(server_coroutine())    
    task4 = asyncio.create_task(square_root(18))
    task5 = asyncio.create_task(divide_by_zero())
    # r1 = await task1
    # if any([isinstance(item, Exception) for item in r1]):
    #     print("Exception:", r1)
    # r2 = await task2
    # return [r1, r2]
    return await asyncio.gather(task1, task2, task3, task4, task5, return_exceptions=False)

async def server_coroutine():
    # simulate server doing stuff by sleeping
    await asyncio.sleep(20)
    print("Sleep completed!")
    return "Sleep completed"

async def divide_by_zero():
    await asyncio.sleep(1)
    return 1/0    # simulate error   

async def main3():            
    server_task = asyncio.create_task(server_coroutine())    
    divide_task = asyncio.create_task(divide_by_zero())
    await server_task
    await divide_task

responses = asyncio.run(main3())
print("RESPONSES", responses)
