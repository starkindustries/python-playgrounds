import threading
import time

class StoppableThread(threading.Thread):
    def __init__(self):
        super(StoppableThread, self).__init__(target=self.foo)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def foo(self):
        while not self._stop_event.is_set():
            print('Hello, world!')
            time.sleep(1)  # sleep for 1 second to avoid printing too fast.

# Initialize the thread
thread = StoppableThread()

# Set the target and arguments
# thread.target = foo
# thread.args = (thread._stop_event,)

# Start the thread
thread.start()

# Do something...
time.sleep(10)  # Sleep for 5 seconds, during which the other thread will print 'Hello, world!'

# Now stop the thread
print("Times up! Stopping thread!")
thread.stop()

# Optionally, wait for the thread to stop before proceeding (join ensures the thread has finished)
thread.join()
