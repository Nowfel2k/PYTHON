import socket

host = 'localhost'
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print("\nServer listing on port",port)
s.listen(1)
connection, clientAddress = s.accept()
print(clientAddress)
print(str(clientAddress))
connection.send(b"Wasup my nigaaa")
connection.send("Hello".encode())
s.close()
