# Server Logging Configuration

# Note on dictConfig() vs fileConfig()
# https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
# Documentation recommends dictConfig() over fileConfig() stating:
# the fileConfig() API is older than the dictConfig() API and does not provide
# functionality to cover certain aspects of logging. For example, you
# cannot configure Filter objects

# References
# https://www.zopatista.com/python/2019/05/11/asyncio-logging/s
# https://rob-blackbourn.medium.com/how-to-use-python-logging-queuehandler-with-dictconfig-1e8b1284e27a
# https://github.com/rob-blackbourn/medium-queue-logging/blob/master/examples/main.py


import logging.config
import logging.handlers
import queue
import atexit


# This function resolves issues when using `cfg://handlers.[name]` where
# QueueListenerHandler complains that `cfg://handlers.[name]` isn't a handler.
# Refers to this line in LOGGING_CONFIG:
# 'handlers': ['cfg://handlers.console', 'cfg://handlers.file']
def _resolve_handlers(l):
    if not isinstance(l, logging.config.ConvertingList):
        return l

    # Indexing the list performs the evaluation.
    return [l[i] for i in range(len(l))]


class QueueListenerHandler(logging.handlers.QueueHandler):
    def __init__(
        self,
        handlers,
        respect_handler_level=False,
        auto_run=True,
        queue=queue.Queue(-1),
    ):
        super().__init__(queue)
        handlers = _resolve_handlers(handlers)
        self._listener = logging.handlers.QueueListener(
            self.queue, *handlers, respect_handler_level=respect_handler_level
        )
        if auto_run:
            self.start()
            atexit.register(self.stop)

    def start(self):
        self._listener.start()

    def stop(self):
        self._listener.stop()

    def emit(self, record):
        return super().emit(record)


JSON_FORMAT = """{
    "time": "%(asctime)s",
    "process_id": "%(process)s", 
    "filename": "%(filename)s",
    "line_number": "%(lineno)d",
    "debug_level": "%(levelname)s",
    "message": "%(message)s",
}"""

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] [%(process)s] [%(filename)s:%(lineno)d] %(levelname)s - %(message)s",
            "datfmt": "%y-%m-%d %H:%M:%S",
            "validate": True,
        },
        "json": {
            "format": JSON_FORMAT,
            "datfmt": "%y-%m-%d %H:%M:%S",
            "validate": True,
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "standard",
            "level": "DEBUG",
            "filename": "server.log",
        },
        "jsonfile": {
            "class": "logging.FileHandler",
            "formatter": "json",
            "level": "DEBUG",
            "filename": "server_log.json",
        },
        "queue_listener": {
            "class": "server_logging_config.QueueListenerHandler",
            "handlers": [
                "cfg://handlers.console",
                "cfg://handlers.file",
                "cfg://handlers.jsonfile",
            ],
        },
    },
    "loggers": {
        "server": {
            "handlers": ["queue_listener"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

# To use, add following in file:
# import logging
# logger = logging.getLogger("server")
# logger.debug('Hello logger')
