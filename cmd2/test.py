import argparse
import cmd2

def get_choices_from_database():
    # This is where you'd get the choices from the database
    # I'm using hardcoded values here for simplicity
    return ['option1', 'option2', 'option3']

def make_choices_provider(choices):
    def choices_provider(text, line, begidx, endidx):
        """Provides choices for argument completion."""
        return choices
    return choices_provider

class App(cmd2.Cmd):
    def __init__(self):
        super().__init__()

    def setup_parser(self):
        choices = get_choices_from_database()
        parser = argparse.ArgumentParser()
        parser.add_argument('-o', '--option', choices=make_choices_provider(choices))
        return parser

    def do_something(self, args):
        """Do something with the provided options."""
        parser = self.setup_parser()
        parsed_args = parser.parse_args(args)
        print(parsed_args.option)

if __name__ == "__main__":
    app = App()
    app.cmdloop()