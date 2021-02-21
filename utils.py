import re
import sys
from socket import socket, AF_INET, SOCK_STREAM
import json
import log.client_log_config
import logging

logger_client = logging.getLogger('client_log')

with open('configs.json', 'r') as file:
    CONFIGS = json.load(file)


def get_ip_and_port(server=False):
    if '-a' in sys.argv:
        ip = sys.argv[sys.argv.index('-a') + 1]
        if not re.match(r'^(([1-9]?\d|1\d\d|25[0-5]|2[0-4]\d)\.){3}([1-9]?\d|1\d\d|25[0-5]|2[0-4]\d)$', ip):
            logger_client.critical('Неверный формат ip-адреса')
            raise Exception('Введите ip в формате ipv4!')
    else:
        ip = CONFIGS['SERV_IP']

    try:
        if '-p' in sys.argv:
            port = int(sys.argv[sys.argv.index('-p') + 1])
            if CONFIGS['MIN_VALUE_FOR_PORT'] > port or port > CONFIGS['MAX_VALUE_FOR_PORT']:
                logger_client.critical('Неверное значение порта!')
                raise Exception('Значение порта должно быть в пределах от 1024 до 65535')
        else:
            port = CONFIGS['PORT']
        sock = socket(AF_INET, SOCK_STREAM)
        if server:
            ip = ''
            sock.bind((ip, port))
            sock.listen(CONFIGS['MAX_CLIENTS_TO_CONNECT'])
        return port, ip, sock
    except ValueError:
        logger_client.critical('Неверное значение порта!')
        print('Порт должен содержать в себе только цифры от 1024 до 65535!')
