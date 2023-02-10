import os
import socket
import threading

def file_handler(connection_socket):
    try:
        message = connection_socket.recv(buffer_size).decode('utf-8')
        # print(message.split()[0], ':', message.split()[1], ':', path)
        file_name = message.split()[1]
        f = open(file_name[1:])
        data = f.read(buffer_size)
        # print(data)
        connection_socket.send('\nHTTP/1.1 200 OK\n'.encode('utf-8'))
        connection_socket.send('Content-Type: text/html; charset=utf-8\n\n'.encode('utf-8'))
        connection_socket.send(data.encode('utf-8'))
        connection_socket.close()
    except:
        # print ('Error')
        f = open('404.html')
        data = f.read(buffer_size)
        connection_socket.send('\nHTTP/1.1 404 Not Found\n'.encode('utf-8'))
        connection_socket.send('Content-Type: text/html; charset=utf-8\n\n'.encode('utf-8'))
        connection_socket.send(data.encode('utf-8'))
        connection_socket.close()

server_ip = '216.171.56.60'
server_port = 7857
buffer_size = 1024
path = os.path

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))

server_socket.listen()

# print('The server is ready to receive')
# print(os.listdir(path))
# print(os.path.basename(path))

while True:
    connection_socket, addr = server_socket.accept()
    threading.Thread(target=file_handler, args=(connection_socket,)).start()
    