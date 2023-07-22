import socket
import threading


HOST = '127.0.0.1'
PORT = 1234


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        
        data = client_socket.recv(1024).decode()
        print(data, end='')


threading.Thread(target=receive_messages).start()

while True:
    message = input('>')
    client_socket.send(f'{message}\n'.encode())
