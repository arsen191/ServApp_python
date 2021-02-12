import time
from utils import get_ip_and_port


PORT, SERV_IP, s = get_ip_and_port(server=True)


def main():
    while True:
        client, addr = s.accept()
        print(f'Получен запрос на соединение от {addr}')
        msg_from_client = client.recv(4096)
        try:
            print(msg_from_client.decode('utf-8'))
        except UnicodeDecodeError:
            print('Сообщение не удалось расшифровать')
        timestr = time.ctime(time.time()) + '\n' + "привет клиент!"
        client.send(timestr.encode('utf-8'))
        client.close()


if __name__ == "__main__":
    main()

