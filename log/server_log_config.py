import logging
from logging import handlers

logger = logging.getLogger('server_log')

formatter = logging.Formatter("%(asctime)s %(levelname)-10s %(module)s %(message)s")

file_handler = handlers.TimedRotatingFileHandler('serverapp.log', interval=1, when="D", utc=True)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
