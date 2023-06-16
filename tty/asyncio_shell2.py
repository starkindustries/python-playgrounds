import sys
import asyncio
import cmd2
import logging

class App(cmd2.Cmd):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.stdin_copy = os.fdopen(os.dup(sys.stdin.fileno()), 'rb', 0)
        self.shutdown = False
        self.host = "127.0.0.1"
        self.port = 9000

    def do_async_task(self, args):
        asyncio.run(self.my_async_function(), debug=True)  #! DEBUG IS ON!!!
        print("async_task completed!")
        self.shutdown = False
    
    async def my_async_function(self):
        self.stdin_reader = asyncio.StreamReader()
        r_protocol = asyncio.StreamReaderProtocol(self.stdin_reader)
        loop = asyncio.get_event_loop()
        await loop.connect_read_pipe(lambda: r_protocol, sys.stdin)

        try:
            self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
        except Exception as e:
            print(f"ERROR on connecting to server: {e}")
            return
        # await asyncio.gather(self.ReadTaskEntry(), self.WriteTaskEntry())
        await self.WriteTaskEntry()

    # async def ReadTaskEntry(self):
    #     while not self.shutdown:
    #         try:
    #             data = await asyncio.wait_for(self.reader.read(1024), timeout=1.0)
    #             if len(data) == 0:
    #                 break
    #             sys.stdout.buffer.write(data)
    #             sys.stdout.buffer.flush()
    #         except TimeoutError:
    #             pass

    async def WriteTaskEntry(self):
        while not self.shutdown:
            single_char_array = await self.stdin_reader.read(1024)
            decoded_char = single_char_array.decode()
            decoded_char = decoded_char.strip()
            print(f"char:[{decoded_char}]", end="", flush=True)
            if decoded_char == "x":
                print("Shutting down..")
                self.shutdown = True                
                break
            
            self.writer.write(single_char_array)
            await self.writer.drain()


logging.basicConfig(level=logging.DEBUG)
app = App()
app.cmdloop()
