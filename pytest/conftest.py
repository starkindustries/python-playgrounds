def pytest_addoption(parser):
    parser.addoption("--name", action="store", default="world", help="name to use in hello function")