import json
import select
import time
import logging
from log_decorator import Log
from utils import get_ip_and_port

logger = logging.getLogger('server_log')


def read_requests(r_list, clients):
    responses = {}
    for sock in r_list:
        try:
            data = sock.recv(4096).decode('utf-8')
            responses[sock] = handle_message(data)
            print(responses)
        except:
            clients.remove(sock)
    return responses


def write_responses(requests, w_list, clients):
    for sock in w_list:
        for _, req in requests.items():
            try:
                resp = req.encode('utf-8')
                sock.send(resp)
            except:
                sock.close()
                clients.remove(sock)


@Log()
def main():
    clients = []
    sock = get_ip_and_port(server=True)
    while True:
        try:
            client, addr = sock.accept()
            print(f'Получен запрос на соединение от {addr}')
            client.send(json.dumps({"action": "probe", "time": time.time()}).encode('utf-8'))
            clients.append(client)
        except OSError:
            pass
        finally:
            r_list, w_list = [], []
            try:
                r_list, w_list, e_list = select.select(clients, clients, [], 1)
            except:
                pass

            requests = read_requests(r_list, clients)
            if requests:
                write_responses(requests, w_list, clients)


def handle_message(msg):
    message = json.loads(msg)
    if message.get('action') == 'presence' and message.get('time') and message.get('type') and message.get('user'):
        return json.dumps({'response': 200, 'time': time.time(), 'alert': 'OK'})
    elif message.get('action') == 'msg' and message.get('time') and message.get('to') and message.get('from') \
            and message.get('message'):
        return json.dumps(
            {'action': 'msg', 'time': time.time(), 'to': message.get('to'), 'from': message.get('from'), "message": message.get('message')})
    else:
        return json.dumps({'response': 400, 'time': time.time(), 'error': 'неправильный запрос/JSON-объект'})


if __name__ == "__main__":
    print("server started!")
    main()
