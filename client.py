import socket

def start_client(host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print("Соединение с сервером установлено")

        while True:
            message = input("Введите сообщение для отправки серверу ('exit' для выхода) ")
            if message.lower() == 'exit':
                break

            client_socket.sendall(message.encode())
            print("Сообщение отправлено серверу", message)

            data = client_socket.recv(1024)
            print("Сообщение получено от сервера", data.decode())

    except ConnectionError:
        print("Ошибка соединения с сервером")
    finally:
        client_socket.close()
        print("Соединение с сервером разорвано")

start_client()
