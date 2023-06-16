import curses
import threading
import time


def print_loop():
    for i in range(10):
        with lock:
            stdscr.addstr(0, 0, f"Count: {i}")
            stdscr.refresh()
        time.sleep(1)

def input_loop():
    while True:
        with lock:
            c = stdscr.getch()
        if c != curses.ERR:
            stdscr.move(1, 0)
            stdscr.clrtoeol()
            stdscr.addstr(1, 0, f"You typed: {chr(c)}")
            stdscr.refresh()
        if c == ord('q'):
            break

# Initialize curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

# Lock for accessing the screen
lock = threading.Lock()

# Create and start the threads
print_thread = threading.Thread(target=print_loop)
input_thread = threading.Thread(target=input_loop)

print_thread.start()
input_thread.start()

# Wait for the threads to finish
print_thread.join()
input_thread.join()

# Clean up curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
