from utils import get_ip_and_port


def main():
    try:
        port, serv_ip, s = get_ip_and_port()
        s.connect((serv_ip, port))
        msg = 'Привет, сервер!'
        s.send(msg.encode('utf-8'))
        data = s.recv(4096)
        s.close()
        try:
            print(data.decode('utf-8'))
        except UnicodeDecodeError:
            print('Сообщение от сервера принято в другой кодировке, расшифровать не удалось')
    except ConnectionRefusedError:
        print("Возможно вы ошиблись адресом подключения, проверьте передаваемые параметры!")
    except TypeError:
        print("Проверьте правильность введенных данных!")


if __name__ == '__main__':
    main()
