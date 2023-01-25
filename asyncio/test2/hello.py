import asyncio

async def func():
  print('run some task code')

async def run(loop):
  task = asyncio.create_task(func())
  while True:
    await asyncio.sleep(1)
    print('ping an external api')

loop = asyncio.get_event_loop()
loop.run_until_complete(run(loop))
loop.run_forever()