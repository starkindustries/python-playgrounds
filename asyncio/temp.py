import asyncio

async def server_coroutine():
    # simulate server doing stuff by sleeping
    await asyncio.sleep(2)
    print("Sleep completed!")
    return "Sleep completed"

async def divide_by_zero():
    return 1/0    # simulate error

async def main(): 
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(server_coroutine())    
        task_group.create_task(divide_by_zero())

responses = asyncio.run(main())
print("RESPONSES", responses)

