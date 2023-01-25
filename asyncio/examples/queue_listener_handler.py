# examples/QueueListenerHandler.py
import logging.config
import logging.handlers
import queue
import atexit


def _resolve_handlers(l):
    if not isinstance(l, logging.config.ConvertingList):
        return l

    # Indexing the list performs the evaluation.
    return [l[i] for i in range(len(l))]


class QueueListenerHandler(logging.handlers.QueueHandler):

    def __init__(self, handlers, respect_handler_level=False, auto_run=True, queue=queue.Queue(-1)):
        super().__init__(queue)
        handlers = _resolve_handlers(handlers)
        self._listener = logging.handlers.QueueListener(
            self.queue,
            *handlers,
            respect_handler_level=respect_handler_level)
        if auto_run:
            self.start()
            atexit.register(self.stop)


    def start(self):
        self._listener.start()


    def stop(self):
        self._listener.stop()


    def emit(self, record):
        return super().emit(record)