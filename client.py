import json
import logging
import time

from log_decorator import Log
from utils import get_ip_and_port
import log.client_log_config

logger = logging.getLogger('client_log')


@Log()
def main():
    try:
        port, serv_ip, s = get_ip_and_port()
        s.connect((serv_ip, port))
        msg = create_presence_message('guest')
        s.send(msg.encode('utf-8'))
        data = s.recv(4096)
        s.close()
        try:
            print(handle_response(data.decode('utf-8')))
            logger.info('Получено сообщение от сервера!')
        except UnicodeDecodeError:
            logger.error('Сообщение от сервера принято в другой кодировке, расшифровать не удалось')
    except ConnectionRefusedError:
        logger.critical('Возможно вы ошиблись адресом подключения, проверьте передаваемые параметры!')
    except TypeError:
        logger.critical('Проверьте правильность введенных данных!')


def create_presence_message(user):
    message = {
        "action": "presence",
        "time": time.time(),
        "type": "status",
        "user": {
            "account_name": user,
            "status": "I am here!"
        }
    }
    return json.dumps(message)


def handle_response(message):
    msg = json.loads(message)
    if msg.get("response") == 200:
        return 200
    return 400


if __name__ == '__main__':
    main()
