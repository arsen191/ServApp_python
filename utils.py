import dis
import inspect
import re
import sys
from socket import socket, AF_INET, SOCK_STREAM
import json
import logging

logger_client = logging.getLogger('client_log')

with open('configs.json', 'r') as file:
    CONFIGS = json.load(file)


def get_ip_and_port(server=False):
    if '-a' in sys.argv:
        ip = sys.argv[sys.argv.index('-a') + 1]
        if not re.match(
            r'^(([1-9]?\d|1\d\d|25[0-5]|2[0-4]\d)\.){3}([1-9]?\d|1\d\d|25[0-5]|2[0-4]\d)$',
                ip):
            logger_client.critical('Неверный формат ip-адреса')
            raise ValueError('Введите ip в формате ipv4!')
    else:
        ip = CONFIGS['SERV_IP']

    try:
        if '-p' in sys.argv:
            port = int(sys.argv[sys.argv.index('-p') + 1])
            # if port < CONFIGS['MIN_VALUE_FOR_PORT'] or port > CONFIGS['MAX_VALUE_FOR_PORT']:
            #     logger_client.critical('Неверное значение порта!')
            #     raise ValueError(
            #         'Значение порта должно быть в пределах от 1024 до 65535')
        else:
            port = CONFIGS['PORT']
        sock = socket(AF_INET, SOCK_STREAM)
        if server:
            ip = ''
            sock.bind((ip, port))
            sock.listen(CONFIGS['MAX_CLIENTS_TO_CONNECT'])
            sock.settimeout(0.2)
            return port, sock
        return port, ip, sock
    except ValueError:
        logger_client.critical('Неверное значение порта или ip-адреса')
        print('Порт должен содержать в себе только цифры от 1024 до 65535!')


def find_forbidden_methods_call(func, method_names):
    for instr in dis.get_instructions(func):
        if instr.opname == 'LOAD_METHOD' and instr.argval in method_names:
            return instr.argval


class Verifier(type):
    forbidden_method_names_for_client = ('accept', 'listen', )
    forbidden_method_names_for_server = ('connect', )

    def __new__(cls, name, bases, class_dict):
        for _, value in class_dict.items():
            if inspect.isfunction(value):
                method_name = find_forbidden_methods_call(value,
                    cls.forbidden_method_names_for_client if name == 'Client' else cls.forbidden_method_names_for_server)
                if method_name:
                    raise ValueError(
                        f'called forbidden method "{method_name}"')
            elif isinstance(value, socket) and name == 'Client':
                raise ValueError(
                    'Socket object cannot be defined in class definition')
        return type.__new__(cls, name, bases, class_dict)
