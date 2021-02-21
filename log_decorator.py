import logging
import log.client_log_config


class Log:
    def __init__(self):
        self.logger = logging.getLogger('logger_decorator')
        formatter = logging.Formatter("%(asctime)s %(funcName)s %(message)s")

        file_handler = logging.FileHandler('app.log', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.INFO)

    def __call__(self, func):
        def decorated(*args, **kwargs):
            self.logger.info('Перехват функции')
            res = func(*args, **kwargs)
            return res
        return decorated
