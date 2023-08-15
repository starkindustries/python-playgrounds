import threading
import time

class StoppableThread(threading.Thread):
    def __init__(self):
        super().__init__(target=self.run_thread)
        self._stop_event = threading.Event()
        # self.target = self.run_thread
        # self.args = ()

    def run_thread(self):
        while not self.stopped():
            print('Hello, world!')
            time.sleep(1)

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

# Initialize the thread
thread = StoppableThread()

# Start the thread
thread.start()

# Do something...
time.sleep(5)

# Now stop the thread
thread.stop()

# Optionally, wait for the thread to stop before proceeding (join ensures the thread has finished)
thread.join()
