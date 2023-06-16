import pyautogui

class UserGuide:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def write_section(self, title, desc, command):
        self.file.write(f"## {title}\n\n{desc}\n\n`{command}`\n\n")

def demo_hello(user_guide):
    title = "Feature Hello"
    desc = "This is how you use feature hello:"
    command = "echo helloworld"
    user_guide.write_section(title, desc, command)
    pyautogui.write(command)

if __name__ == "__main__":
    with UserGuide('UserGuide.md') as user_guide:
        demo_hello(user_guide)
