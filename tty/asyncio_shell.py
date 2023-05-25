import sys
import asyncio
import cmd2
import termios
import tty
import os

class App(cmd2.Cmd):
    def do_async_task(self, args):
        # Save the original stdin
        original_stdin = sys.stdin

        # Your asyncio code here
        asyncio.run(self.my_async_function())

        # Restore the original stdin
        sys.stdin = original_stdin

    async def my_async_function(self):
        # This is just an example function
        loop = asyncio.get_event_loop()
        print(f"{sys.stdin.fileno()=}")
        # stdin_fd = os.dup(sys.stdin.fileno())
        stdin_fd = sys.stdin.fileno()
        # print(f"{stdin_fd=}")
        stdin_file = os.fdopen(stdin_fd, 'rb', 0)
        # old_stdin_settings = termios.tcgetattr(stdin_fd)

        if sys.stdin.isatty():
            print("Setting tty to pass ctrl-c through")                        
            tty.setcbreak(stdin_fd)
            # Need to pass through CTRL-C and other control sequences
            new_stdin_settings = termios.tcgetattr(stdin_fd)
            new_stdin_settings[3] = new_stdin_settings[3] & ~termios.ISIG
            new_stdin_settings[3] = new_stdin_settings[3] & ~termios.ECHO
            termios.tcsetattr(stdin_fd, termios.TCSANOW, new_stdin_settings)
        
        self.stdin_reader = asyncio.StreamReader()
        r_protocol = asyncio.StreamReaderProtocol(self.stdin_reader)
        await loop.connect_read_pipe(lambda: r_protocol, stdin_file)

        w_transport, w_protocol = await loop.connect_write_pipe(
            asyncio.streams.FlowControlMixin, sys.stdout
        )
        self.stdout_writer = asyncio.StreamWriter(
            w_transport, w_protocol, self.stdin_reader, loop
        )

        user_input = await self.stdin_reader.read(1024)
        print(f"User entered: {user_input}")

        # Restore original stdin settings
        # termios.tcsetattr(stdin_fd, termios.TCSANOW, old_stdin_settings)
        # print(f"{sys.stdin.fileno()=}")
        
        print("Async task completed")

app = App()
app.cmdloop()
