
"""A simple cmd2 application."""
import cmd2


class FirstApp(cmd2.Cmd):
    """A simple cmd2 application."""

    def do_hello_world(self, _: cmd2.Statement):
        self.poutput('Hello World')

if __name__ == '__main__':
    import sys
    c = FirstApp()
    sys.exit(c.cmdloop())



# In this example, the MyApp class is a subclass of cmd2.Cmd, which provides the basic functionality for creating a command-line interface. The do_hello method is a command that can be executed by the user. When the command is run, it simply prints "Hello!" to the console.

# You can run the code by typing python yourfilename.py in your terminal, once the script is running you can type hello and press enter to see the output, you can try other commands that you can define in the similar way.

# You can also use help command to see the list of commands and help commandname to see the description of the command.
