from multiprocessing import Process, Queue
import asyncio

def run_in_new_process(q):
    result = asyncio.run(my_async_function())
    q.put(result)

async def my_async_function():
    print("Running async function")
    return "result"

if __name__ == "__main__":
    q = Queue()
    p = Process(target=run_in_new_process, args=(q,))
    p.start()
    result = q.get()
    p.join()
    print(f"Got result: {result}")
