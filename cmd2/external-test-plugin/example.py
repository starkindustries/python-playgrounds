import cmd2
class ExampleApp(cmd2.Cmd):
    """An class to show how to use a plugin"""
    def __init__(self, *args, **kwargs):
        # gotta have this or neither the plugin or cmd2 will initialize
        super().__init__(*args, **kwargs)

    def do_something(self, arg):
        # self.last_result = 5
        self.last_result = { "foo" : 5, "bar" : 10 }
        self.poutput('this is the something command')