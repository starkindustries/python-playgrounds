import queue
import logging
from logging.handlers import QueueHandler, QueueListener

# https://www.zopatista.com/python/2019/05/11/asyncio-logging/
# https://rob-blackbourn.medium.com/how-to-use-python-logging-queuehandler-with-dictconfig-1e8b1284e27a

log_queue = queue.Queue(-1)
queue_handler = QueueHandler(log_queue)

logger = logging.getLogger()
logger.addHandler(queue_handler)

console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(threadName)s: %(message)s')
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("queue_example.log")
file_handler.setFormatter(formatter)

listener = QueueListener(log_queue, console_handler, file_handler)
listener.start()

logger.warning('Look out!')

listener.stop()