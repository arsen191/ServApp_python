import json
import time
import logging
from log_decorator import Log
from utils import get_ip_and_port, get_message, CONFIGS
import log.server_log_config

logger = logging.getLogger('server_log')
PORT, SERV_IP, s = get_ip_and_port(server=True)


@Log()
def main():
    while True:
        client, addr = s.accept()
        print(f'Получен запрос на соединение от {addr}')
        msg_from_client = client.recv(4096).decode('utf-8')
        handle_msg = ''
        try:
            print(msg_from_client)
            handle_msg = handle_message(msg_from_client)
            logger.info('Получено сообщение от клиента!')
        except UnicodeDecodeError:
            logger.error('Сообщение не удалось расшифровать')
            print('Сообщение не удалось расшифровать')
        client.send(handle_msg.encode('utf-8'))
        client.close()


def handle_message(msg):
    message = json.loads(msg)
    if message.get('action') == 'presence' and message.get('time') and message.get('type') and message.get('user'):
        return json.dumps({'response': 200, 'time': time.time(), 'alert': 'OK'})
    else:
        return json.dumps({'response': 400, 'time': time.time(), 'error': 'неправильный запрос/JSON-объект'})


if __name__ == "__main__":
    main()

