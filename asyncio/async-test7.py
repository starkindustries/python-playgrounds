import asyncio
import time

async def async_task(var):
    print("Starting async task")
    await asyncio.sleep(5)
    print("Finished async task: ", var)

def sync_task(var):
    print("Starting sync task")
    time.sleep(3)
    print("Finished sync task: ", var)

async def main():
    # Start the async task
    async_task_future = asyncio.create_task(async_task("a"))

    # Run the synchronous task in a separate thread
    sync_task_future = asyncio.to_thread(sync_task, "b")

    # Wait for both tasks to complete
    await asyncio.gather(async_task_future, sync_task_future)

if __name__ == "__main__":
    asyncio.run(main())
