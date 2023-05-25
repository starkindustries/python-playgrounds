import tty
import os
import termios
import sys

def get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        ch = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def detect_ctrl_t():
    char = get_char()
    return char == '\x14'

def control_key(letter):
    return chr(ord(letter.upper()) & 0x1F)

while True:
    if detect_ctrl_t():
        print("Ctrl detected")
        break

print(f"ctrl u : {control_key('u')}")
print(f"ctrl v : {control_key('v')}")