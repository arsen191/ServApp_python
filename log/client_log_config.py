import logging

logger = logging.getLogger('client_log')

formatter = logging.Formatter("%(asctime)s %(levelname)-10s %(module)s %(message)s")

file_handler = logging.FileHandler('clientapp.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
