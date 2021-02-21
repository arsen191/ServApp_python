import time
import logging

from log_decorator import Log
from utils import get_ip_and_port
import log.server_log_config

logger = logging.getLogger('server_log')

PORT, SERV_IP, s = get_ip_and_port(server=True)


@Log()
def main():
    while True:
        client, addr = s.accept()
        print(f'Получен запрос на соединение от {addr}')
        msg_from_client = client.recv(4096)
        try:
            print(msg_from_client.decode('utf-8'))
            logger.info('Получено сообщение от клиента!')
        except UnicodeDecodeError:
            logger.error('Сообщение не удалось расшифровать')
            print('Сообщение не удалось расшифровать')
        timestr = time.ctime(time.time()) + '\n' + "привет клиент!"
        client.send(timestr.encode('utf-8'))
        client.close()


if __name__ == "__main__":
    main()

