import json
import select
import time
import logging
from log.log_decorator import Log
from utils import get_ip_and_port, Verifier, CONFIGS

logger = logging.getLogger('server_log')


class PortValidator:

    def __init__(self, default=CONFIGS['PORT']):
        self.default = default
        self._value = None

    def __get__(self, instance, owner):
        return self._value or self.default

    def __set__(self, instance, value):
        if isinstance(value, int) and 1024 <= value <= 65535:
            self._value = value
            return
        raise ValueError('Значение порта должно быть целым числом, больше 1024 и меньше 65535')


class Server(metaclass=Verifier):
    """
    Серверная часть
    """
    port = PortValidator()

    def __init__(self, sock):
        self.sock = sock
        self.clients = []

    @Log()
    def main(self):
        print("server started!")
        while True:
            try:
                client, addr = self.sock.accept()
                print(f'Получен запрос на соединение от {addr}')
                client.send(json.dumps({"action": "probe", "time": time.time()}).encode('utf-8'))
                self.clients.append(client)
            except OSError:
                pass
            finally:
                r_list, w_list = [], []
                try:
                    r_list, w_list, e_list = select.select(self.clients, self.clients, [], 0)
                except:
                    pass

                requests = self.read_requests(r_list, self.clients)
                if requests:
                    self.write_responses(requests, w_list)

    def read_requests(self, r_list, clients):
        responses = {}
        for sock in r_list:
            try:
                data = sock.recv(4096).decode('utf-8')
                responses[sock] = self.handle_message(data)
                print(responses)
            except:
                clients.remove(sock)
        return responses

    def write_responses(self, requests, w_list):
        for sock in w_list:
            for _, req in requests.items():
                try:
                    if _ is sock and 'response' in req:
                        resp = req.encode('utf-8')
                        sock.send(resp)
                    elif 'response' in req:
                        continue
                    else:
                        resp = req.encode('utf-8')
                        sock.send(resp)
                except:
                    sock.close()
                    self.clients.remove(sock)

    def handle_message(self, msg):
        message = json.loads(msg)
        if message.get('action') == 'presence' and message.get('time') and message.get('type') and message.get('user'):
            return json.dumps({'response': 200, 'time': time.time(), 'alert': 'OK'})
        elif message.get('action') == 'msg' and message.get('time') and message.get('to') and message.get('from') \
                and message.get('message'):
            return json.dumps(
                {'action': 'msg', 'time': time.time(), 'to': message.get('to'), 'from': message.get('from'),
                 "message": message.get('message')})
        else:
            return json.dumps({'response': 400, 'time': time.time(), 'error': 'неправильный запрос/JSON-объект'})


if __name__ == "__main__":
    p, s = get_ip_and_port(server=True)
    server = Server(s)
    server.port = p
    server.main()

