import threading
import time

class StoppableThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.foo = "foo"
        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            print('Hello, world!')
            time.sleep(1)

    def stop(self):
        self._stop_event.set()

# Initialize the thread
thread = StoppableThread()

# Start the thread
thread.start()

time.sleep(1)

for i in range(5):
    print(thread.foo)
    time.sleep(1)

# Do something...
time.sleep(5)

# Now stop the thread
thread.stop()

# Optionally, wait for the thread to stop before proceeding
thread.join()
