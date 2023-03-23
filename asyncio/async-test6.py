import asyncio

async def run_foo():
    while True:
        print("Foo counting numbers..")
        for i in range(10000000):
            a = i + i
        # this line is required otherwise foo will block the event loop
        await asyncio.sleep(0)

async def run_bar():
    while True:
        print("  Bar counting sheep..")
        await asyncio.sleep(1)


async def myapp():
    await asyncio.gather(
        run_foo(), run_bar()
    )

if __name__ == "__main__":
    asyncio.run(myapp())