import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message, _ = client_socket.recvfrom(1024)
            print("\nСообщение:", message.decode())
        except:
            print("Ошибка при получении сообщения")
            break

def start_client(server_host='127.0.0.1', server_port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    try:
        while True:
            message = input("Введите сообщение ('exit' для выхода): ")
            if message.lower() == 'exit':
                print("Выход из чата")
                break

            client_socket.sendto(message.encode(), (server_host, server_port))

    except KeyboardInterrupt:
        print("\nКлиент остановлен вручную")
    finally:
        client_socket.close()
        print("Клиент завершил работу")

start_client()
