import logging
import logging.config

# Note https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
# The fileConfig() API is older than the dictConfig() API and does not provide functionality to cover certain aspects of logging. For example, you cannot configure Filter objects

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
        'stream': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'DEBUG',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'level': 'DEBUG',
            'filename': 'server.log'
        }
    },
    'loggers': { 
        'server': { 
            'handlers': ['stream', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
    } 
}

# Run once at startup:
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("server")
# Include in each module:
# log = logging.getLogger(__name__)
# log.debug("Logging is configured.")