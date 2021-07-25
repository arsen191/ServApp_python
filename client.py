import json
import logging
import sys
import threading
import time
from utils import get_ip_and_port, Verifier

logger = logging.getLogger('client_log')


class Client(metaclass=Verifier):
    """
    Клиентская часть
    """

    def __init__(self, port, serv_ip, sock):
        self.port = port
        self.serv_ip = serv_ip
        self.sock = sock
        self.person = input('Введите свое имя: ')

    def main(self):
        self.sock.connect((self.serv_ip, self.port))
        # self.create_presence_message()
        self.read_and_parse_msg()

        sender = threading.Thread(target=self.write_msg, args=(), daemon=True)
        receiver = threading.Thread(target=self.read_and_parse_msg, args=(), daemon=True)
        sender.start()
        receiver.start()

        while True:
            if sender.is_alive() and receiver.is_alive():
                continue
            self.sock.close()
            break

    def write_msg(self):
        while True:
            msg = input('')
            self.sock.send(self.handle_response(msg).encode('utf-8'))

    def read_and_parse_msg(self):
        while True:
            try:
                data = json.loads(self.sock.recv(4096).decode('utf-8'))
                if data.get('action') == 'probe':
                    self.create_presence_message()
                elif data.get('response') == 200:
                    print('Подключение к серверу установлено!')
                    break
                elif data.get('action') == 'msg':
                    print(f"\rResponse: {data.get('message')}")
            except KeyboardInterrupt:
                print('Клиентское приложение закрыто')
                sys.exit(1)

    def create_presence_message(self):
        message = {
            "action": "presence",
            "time": time.time(),
            "type": "status",
            "user": {
                "account_name": self.person,
                "status": "I am here!"
            }
        }
        self.sock.send(json.dumps(message).encode('utf-8'))

    def handle_response(self, message):
        return json.dumps({
                "action": "msg",
                "time": time.time(),
                "to": "client",
                "from": self.person,
                "message": message
            })


if __name__ == '__main__':
    p, s_ip, s = get_ip_and_port()
    client = Client(p, s_ip, s)
    client.main()
