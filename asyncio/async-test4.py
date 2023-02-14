import asyncio

async def server_coroutine():
    # simulate server by sleeping
    await asyncio.sleep(20)
    print("server completed!")
    return "server completed"

async def divide_by_zero():
    return 1/0    # simulate error

async def main():            
    server_task = asyncio.create_task(server_coroutine())    
    divide_task = asyncio.create_task(divide_by_zero())
    await server_task
    await divide_task

asyncio.run(main())
