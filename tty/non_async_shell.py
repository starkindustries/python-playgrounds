import sys
import cmd2
import termios
import tty
import os

class App(cmd2.Cmd):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stdin_copy = os.fdopen(os.dup(sys.stdin.fileno()), 'rb', 0)

    def do_async_task(self, args):
        print(f"Before asyncio task: sys.stdin = {sys.stdin}")

        if sys.stdin.isatty():
            print("Setting tty to pass ctrl-c through")                        
            tty.setcbreak(sys.stdin.fileno())
            # Need to pass through CTRL-C and other control sequences
            original_stdin_settings = termios.tcgetattr(sys.stdin.fileno())
            new_stdin_settings = original_stdin_settings[:]
            new_stdin_settings[3] &= ~termios.ISIG
            new_stdin_settings[3] &= ~termios.ECHO
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, new_stdin_settings)

        self.my_function()

        # Restore original terminal settings
        if sys.stdin.isatty():
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, original_stdin_settings)

        print(f"After asyncio task: sys.stdin = {sys.stdin}")

    def my_function(self):
        print(f"{sys.stdin.fileno()=}")

        user_input = self.stdin_copy.read(1024)
        print(f"User entered: {user_input}")
        print("Task completed")


app = App()
print(f"Before cmdloop: sys.stdin = {sys.stdin}")
app.cmdloop()
print(f"After cmdloop: sys.stdin = {sys.stdin}")
