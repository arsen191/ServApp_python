import json
import logging
import sys
import threading
import time
from log_decorator import Log
from utils import get_ip_and_port

logger = logging.getLogger('client_log')


@Log()
def main():
    port, serv_ip, sock = get_ip_and_port()
    sock.connect((serv_ip, port))
    person = input('Введите свое имя: ')
    create_presence_message(person, sock)
    if json.loads(sock.recv(4096).decode('utf-8')).get('response') == 200:
        print('Подключение к серверу установлено!')

    try:
        sender = threading.Thread(target=write_msg, args=(sock, person, ), daemon=True)
        receiver = threading.Thread(target=read_and_parse_msg, args=(sock, ), daemon=True)
        sender.start()
        receiver.start()
    except KeyboardInterrupt:
        sock.close()
    else:
        while True:
            if sender.is_alive() and receiver.is_alive():
                continue
            break


def write_msg(sock, frm):
    while True:
        msg = input('')
        sock.send(handle_response(msg, frm).encode('utf-8'))


def read_and_parse_msg(sock, presence=None):
    while True:
        try:
            data = json.loads(sock.recv(4096).decode('utf-8'))
            if data.get('action') == 'probe':
                sock.send(presence)
            elif data.get('response') == 200:
                print('Подключение к серверу установлено!')
            elif data.get('action') == 'msg':
                print(f"\rResponse: {data.get('message')}")
        except KeyboardInterrupt:
            print('Клиентское приложение закрыто')
            sys.exit(1)


def create_presence_message(user, sock):
    message = {
        "action": "presence",
        "time": time.time(),
        "type": "status",
        "user": {
            "account_name": user,
            "status": "I am here!"
        }
    }
    sock.send(json.dumps(message).encode('utf-8'))


def handle_response(message, frm):
    return json.dumps({
            "action": "msg",
            "time": time.time(),
            "to": "client",
            "from": frm,
            "message": message
        })


if __name__ == '__main__':
    main()
