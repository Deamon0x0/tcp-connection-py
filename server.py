# import socket

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('127.0.0.1', 1234))
# server.listen()

# while True:
#    client, address = server.accept()
#    print(f"connected to {address}")
#    print(client.recv(1024).decode('utf-8'))
#    client.send("hello client".encode('utf-8'))
#    print(client.recv(1024).decode('utf-8'))
#    client.send("bye".encode('utf-8'))
#    client.close()
   
    
import socket

host = '127.0.0.1'
port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))

server.listen()

while True:
    client, address = server.accept()
    print(f"the server is now connecting to {address}")
    print(client.recv(1024).decode('utf-8'))
    client.send("Hello world!".encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
    client.send("server is shutting down...........".encode('utf-8'))
    client.close()
    
    