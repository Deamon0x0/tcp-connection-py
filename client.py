# import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('127.0.0.1', 1234))

# client.send("hello server".encode("utf-8"))
# print(client.recv(1024).decode('utf-8'))
# client.send("bye".encode("utf-8"))
# print(client.recv(1024).decode('utf-8'))
 
 
import socket

host = '127.0.0.1'
port = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

client.send("Requesting demo requests".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))
client.send("bye".encode("utf-8"))
print(client.recv(1024).decode('utf-8'))
 