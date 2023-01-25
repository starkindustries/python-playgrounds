import logging
import logging.config
import server_logging_config

logging.config.dictConfig(server_logging_config.LOGGING_CONFIG)
logger = logging.getLogger("server")

print("main.py online..")
logger.debug("HELLO WORLD")
logger.info("THIS IS AN INFO LOG")