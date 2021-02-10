import sys
from socket import socket, AF_INET, SOCK_STREAM
import time


if '-a' in sys.argv:
    SERV_IP = sys.argv[sys.argv.index('-a') + 1]
else:
    SERV_IP = ''

if '-p' in sys.argv:
    PORT = int(sys.argv[sys.argv.index('-p') + 1])
else:
    PORT = 7777

s = socket(AF_INET, SOCK_STREAM)
s.bind((SERV_IP, PORT))
s.listen(1)

while True:
    client, addr = s.accept()
    print(f'Получен запрос на соединение от {addr}')
    msg_from_client = client.recv(4096)
    print(msg_from_client.decode('utf-8'))
    timestr = time.ctime(time.time()) + '\n' + "привет клиент!"
    client.send(timestr.encode('utf-8'))
    client.close()
