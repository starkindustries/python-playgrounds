# https://cmd2.readthedocs.io/en/latest/plugins/external_test.html

import cmd2_ext_test
from cmd2 import CommandResult
import pytest
from example import ExampleApp

class ExampleAppTester(cmd2_ext_test.ExternalTestMixin, ExampleApp):
    def __init__(self, *args, **kwargs):
        # gotta have this or neither the plugin or cmd2 will initialize
        super().__init__(*args, **kwargs)

@pytest.fixture
def example_app():
    app = ExampleAppTester()
    app.fixture_setup()
    yield app
    app.fixture_teardown()


def test_something(example_app):
    # execute a command
    out = example_app.app_cmd("something")

    # validate the command output and result data
    print(out)

    assert isinstance(out, CommandResult)
    assert str(out.stdout).strip() == 'this is the something command'
    assert out.data == { "foo" : 5, "bar" : 10 }
