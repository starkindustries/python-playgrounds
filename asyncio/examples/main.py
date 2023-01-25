import logging
import logging.config
# import yaml
from examples.my_script1 import do_stuff1
from examples.my_script2 import do_stuff2

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(process)s] [%(filename)s:%(lineno)d] %(levelname)s - %(message)s',
            'datfmt': '%y-%m-%d %H:%M:%S',
            'validate': True
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'DEBUG',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'level': 'DEBUG',
            'filename': 'example3.log'
        },
        'queue_listener': {
            'class': 'examples.QueueListenerHandler',
            'handlers': ['cfg://handlers.console', 'cfg://handlers.file']
        },
    },
    'loggers': { 
        'server': { 
            'handlers': ['queue_listener'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

# LOGGING_CONFIG2 = """
# version: 1
# formatters:
#   simple:
#     format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# handlers:
#   console:
#     class: logging.StreamHandler
#     level: DEBUG
#     formatter: simple
#     stream: ext://sys.stdout
#   file:
#     class: logging.FileHandler
#     filename: 'config_example2.log'
#     formatter: simple
#   queue_listener:
#     class: examples.QueueListenerHandler
#     handlers:
#       - cfg://handlers.console
#       - cfg://handlers.file
# loggers:
#   examples.my_script1:
#     level: DEBUG
#     handlers:
#       - queue_listener
#     propagate: false
#   examples.my_script2:
#     level: WARNING
#     handlers: 
#       - queue_listener
#     propagate: false
# root:
#   level: WARN
#   handlers:
#     - console"""

# logging_config = yaml.load(LOGGING_CONFIG2, Loader=yaml.FullLoader)
# for key, value in logging_config.items():
#     print(key, ":", value)

# logging.config.dictConfig(logging_config)
logging.config.dictConfig(LOGGING_CONFIG)

other_logger = logging.getLogger("foo")

do_stuff1()
do_stuff2()

other_logger.debug("A different debug message")
other_logger.info("A different info message")
other_logger.error("A different error message")

# logging.config.dictConfig(LOGGING_CONFIG)
# logger = logging.getLogger("server")