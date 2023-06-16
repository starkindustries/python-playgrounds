import sys
import asyncio
import cmd2
import os

class App(cmd2.Cmd):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stdin_copy = os.fdopen(os.dup(sys.stdin.fileno()), 'rb', 0)

    def do_async_task(self, args):
        asyncio.run(self.my_async_function())

    async def my_async_function(self):
        loop = asyncio.get_running_loop()
        print(f"{sys.stdin.fileno()=}")
        
        self.stdin_reader = asyncio.StreamReader()
        r_protocol = asyncio.StreamReaderProtocol(self.stdin_reader)
        await loop.connect_read_pipe(lambda: r_protocol, self.stdin_copy)

        user_input = await self.stdin_reader.read(1024)
        print(f"User entered: {user_input}")
        print("Async task completed")


app = App()
app.cmdloop()
