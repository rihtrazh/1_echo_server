import socket

def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    print("Сервер запущен по адресу", host, "на порту", port)

    server_socket.listen(5)
    print("Сервер слушает порт", port)

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print("Клиент подключился", client_address)

            try:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        print("Клиент отключился", client_address)
                        break

                    print("Данные получены от клиента", data.decode())

                    client_socket.sendall(data)
                    print("Данные отправлены клиенту", data.decode())

            except Exception as e:
                print("Произошла ошибка с клиентом", e)
            finally:
                client_socket.close()
                print("Соединение с клиентом закрыто", client_address)

    except KeyboardInterrupt:
        print("\nСервер остановлен вручную")
    finally:
        server_socket.close()
        print("Сервер закрыт")

start_server()
