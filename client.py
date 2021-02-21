import logging

from log_decorator import Log
from utils import get_ip_and_port
import log.client_log_config

logger = logging.getLogger('client_log')

@Log()
def main():
    try:
        port, serv_ip, s = get_ip_and_port()
        s.connect((serv_ip, port))
        msg = 'Привет, сервер!'
        s.send(msg.encode('utf-8'))
        data = s.recv(4096)
        s.close()
        try:
            print(data.decode('utf-8'))
            logger.info('Получено сообщение от сервера!')
        except UnicodeDecodeError:
            logger.error('Сообщение от сервера принято в другой кодировке, расшифровать не удалось')
            # print('Сообщение от сервера принято в другой кодировке, расшифровать не удалось')
    except ConnectionRefusedError:
        logger.critical('Возможно вы ошиблись адресом подключения, проверьте передаваемые параметры!')
        # print("Возможно вы ошиблись адресом подключения, проверьте передаваемые параметры!")
    except TypeError:
        logger.critical('Проверьте правильность введенных данных!')
        # print("Проверьте правильность введенных данных!")


if __name__ == '__main__':
    main()
