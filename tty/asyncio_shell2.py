import asyncio
import cmd2
import threading
import queue

class App(cmd2.Cmd):
    def __init__(self):
        super().__init__()
        self.queue = queue.Queue()

    def do_async_task(self, args):
        async_thread = threading.Thread(target=self.run_async_task, daemon=True)
        async_thread.start()

    def run_async_task(self):
        asyncio.run(self.my_async_function())

    async def my_async_function(self):
        # Replace print statements with self.queue.put
        self.queue.put("Starting async task")
        await asyncio.sleep(2)  # Simulate async work
        self.queue.put("Async task completed")

    def do_check_queue(self, args):
        while not self.queue.empty():
            print(self.queue.get())

app = App()
app.cmdloop()
