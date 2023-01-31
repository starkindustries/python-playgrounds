import logging
import logging.config
import myconfig

logging.config.dictConfig(myconfig.LOGGING_CONFIG)
logger = logging.getLogger("server")

print("main.py online..")
logger.debug("HELLO WORLD")
logger.info("THIS IS AN INFO LOG")