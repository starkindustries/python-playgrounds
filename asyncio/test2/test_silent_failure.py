import asyncio


async def func():
    raise ValueError("encountered some error")


async def run(loop):
    # the `task` var never gets used and also this function
    # never returns. Therefore, the exception does not
    # get raised..
    task = asyncio.create_task(func())
    # solution 1: await the task
    # await asyncio.create_task(func())
    while True:
        await asyncio.sleep(1)
        print("ping an external api")


loop = asyncio.get_event_loop()
loop.run_until_complete(run(loop))
loop.run_forever()
