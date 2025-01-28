import socket

def start_server(host='0.0.0.0', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print("Сервер чата запущен на", host, ":", port)

    clients = set()

    try:
        while True:
            message, client_address = server_socket.recvfrom(1024)
            print(f"Сообщение от {client_address}: {message.decode()}")

            if client_address not in clients:
                clients.add(client_address)
                print(f"Новый клиент добавлен: {client_address}")

            for client in clients:
                if client != client_address:
                    server_socket.sendto(message, client)

    except KeyboardInterrupt:
        print("\nСервер остановлен вручную")
    finally:
        server_socket.close()
        print("Сервер закрыт")

start_server()
