
def test_hello(request):
    name = request.config.getoption("--name")
    print("HELLO WORLD", name) 