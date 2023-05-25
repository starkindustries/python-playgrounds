# example.py

def add_numbers(a: int, b: int) -> int:
    return a + int(b)

result = add_numbers(5, 10)
print(result)

hello: bool | None = None
hello = True
print(hello)