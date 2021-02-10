from socket import socket, AF_INET, SOCK_STREAM
import sys

if '-a' in sys.argv:
    SERV_IP = sys.argv[sys.argv.index('-a') + 1]
else:
    SERV_IP = 'localhost'

if '-p' in sys.argv:
    PORT = int(sys.argv[sys.argv.index('-p') + 1])
else:
    PORT = 7777

s = socket(AF_INET, SOCK_STREAM)
s.connect((SERV_IP, PORT))
msg = 'Привет, сервер!'
s.send(msg.encode('utf-8'))
data = s.recv(4096)
s.close()
print(data.decode('utf-8'))
