import sys
import asyncio
import cmd2
import termios
import tty
import threading

class App(cmd2.Cmd):
    def do_async_task(self, args):
        async_thread = threading.Thread(target=self.run_async_task, daemon=True)
        async_thread.start()

    def run_async_task(self):
        asyncio.run(self.my_async_function())

    async def my_async_function(self):
        loop = asyncio.get_event_loop()

        # Backup old termios settings
        stdin_fd = sys.stdin.fileno()
        old_termios = termios.tcgetattr(stdin_fd)

        try:
            if sys.stdin.isatty():
                print("Setting tty to pass ctrl-c through")            
                tty.setcbreak(stdin_fd)

                # Need to pass through CTRL-C and other control sequences
                new_stdin_settings = termios.tcgetattr(stdin_fd)
                new_stdin_settings[3] = new_stdin_settings[3] & ~termios.ISIG
                new_stdin_settings[3] = new_stdin_settings[3] & ~termios.ECHO
                print("Applying new settings to termios...")
                termios.tcsetattr(stdin_fd, termios.TCSANOW, new_stdin_settings)
                print("Termios settings applied!")
            
            print("Creating asyncio.StreamReader...")
            self.stdin_reader = asyncio.StreamReader()
            r_protocol = asyncio.StreamReaderProtocol(self.stdin_reader)
            
            print("About to connect_read_pipe...")
            await loop.connect_read_pipe(lambda: r_protocol, sys.stdin)
            print("connect_read_pipe completed")

            print("About to connect_write_pipe...")
            w_transport, w_protocol = await loop.connect_write_pipe(
                asyncio.streams.FlowControlMixin, sys.stdout
            )
            print("connect_write_pipe completed")

            self.stdout_writer = asyncio.StreamWriter(
                w_transport, w_protocol, self.stdin_reader, loop
            )

            print("Async task completed")
        finally:
            # Restore old termios settings
            termios.tcsetattr(stdin_fd, termios.TCSANOW, old_termios)
            print("Termios settings restored!")

            if r_protocol:
                print("about to send eof to r_protocol..")
                r_protocol.eof_received()
                print("r_protocol closed!")

            if self.stdout_writer and not self.stdout_writer.is_closing():
                print("Closing stdout_writer")
                self.stdout_writer.close()
                # await self.stdout_writer.wait_closed()
                print("stdout_writer closed!")

app = App()
app.cmdloop()
