import socket
import threading


HOST = '127.0.0.1'
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))


server_socket.listen(5)

print(f'Server listening on {HOST}:{PORT}')

client_sockets = []

def handle_client(client_socket):
    while True:

        data = client_socket.recv(1024).decode()

        for socket in client_sockets:
            socket.send(f'{data}\n'.encode())

        if not data:
            client_sockets.remove(client_socket)
            break

while True:

    client_socket, client_address = server_socket.accept()
    print(f'Client connected from {client_address}')

    client_sockets.append(client_socket)

    threading.Thread(target=handle_client, args=(client_socket,)).start()
