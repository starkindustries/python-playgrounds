import logging
import logging.config
#import copy

# References
# https://www.zopatista.com/python/2019/05/11/asyncio-logging/s
# https://rob-blackbourn.medium.com/how-to-use-python-logging-queuehandler-with-dictconfig-1e8b1284e27a
# https://github.com/rob-blackbourn/medium-queue-logging/blob/master/examples/main.py


import logging.handlers
import queue
import atexit


# This function resolves issues when using `cfg://handlers.[name]` where
# QueueListenerHandler complains that `cfg://handlers.[name]` isn't a handler.
# Refers to this line in LOGGING_CONFIG:
# 'handlers': ['cfg://handlers.console', 'cfg://handlers.file']
def _resolve_handlers(myhandlers):
    print("MY HANDLERS", myhandlers)
    if not isinstance(myhandlers, logging.config.ConvertingList):
        print("RETURNING MYHANDLERS!")
        return myhandlers

    # Indexing the list performs the evaluation.
    temp = []
    for i in range(len(myhandlers)):
        print(f"myhandlers[{i}]: {myhandlers[i]}")
        temp.append(myhandlers[0])
    # temp = [myhandlers[i] for i in range(len(myhandlers))]
    print("INDEXING MY HANDLERS:", temp)
    return temp


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


# LOGGING_CONFIG = {
#     "version": 1,
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#         },
#         "queue_listener": {
#             "class": __name__ + ".QueueListenerHandler",
#             "handlers": [
#                 "cfg://handlers.console"
#             ],
#         },
#     },
#     "loggers": {
#         "server": {
#             "handlers": ["queue_listener"],
#             "level": "DEBUG",
#         },
#     },
# }

JSON_FORMAT = """{
    "time": "%(asctime)s",
    "process_id": "%(process)s", 
    "filename": "%(filename)s",
    "line_number": "%(lineno)d",
    "debug_level": "%(levelname)s",
    "message": "%(message)s"
},"""

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
        "file_cliserver": {
            "class": "logging.FileHandler",
            "formatter": "standard",
            "level": "DEBUG",
            "filename": "cli_server.log",
        },
        "jsonfile_cliserver": {
            "class": "logging.FileHandler",
            "formatter": "json",
            "level": "DEBUG",
            "filename": "cli_server_log.json",
        },         
        "queue_listener": {
            "class": __name__ + ".QueueListenerHandler",
            "handlers": [
                "cfg://handlers.console",
                "cfg://handlers.file",
                "cfg://handlers.jsonfile",
            ],
        },
    },
    "loggers": {
        "cli_server": {
            "handlers": ["console", "file_cliserver", "jsonfile_cliserver"],
            "level": "DEBUG",
            "propagate": False,
        },
        "server": {
            "handlers": ["queue_listener"],
            "level": "DEBUG",
            "propagate": False,
        },        
    },
}

# def test_with_letter(letter_to_test):
#     print("TESTING LETTER:", letter_to_test)
#     try:
#         config_copy = copy.deepcopy(LOGGING_CONFIG)
#         config_copy["handlers"]["queue_listenr"]["handlers"][0] = "cfg://handlers." + letter_to_test
#         config_copy["handlers"][letter_to_test] = config_copy["handlers"]["console"]
#         del config_copy["handlers"]["console"]

#         logging.config.dictConfig(config_copy)
#         logger = logging.getLogger("server")
#         logger.debug("HELLO WORLD")
#     except Exception as error:
#         print("EXCEPTION:", error)


if __name__ == "__main__":
    # test_with_letter("a")
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger("server")
    logger.debug("HELLO WORLD")

    #logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger("cli_server")
    logger.debug("HELLO CLI_SERVER!!")