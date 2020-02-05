import socket

host = 'localhost'
port = 5252
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print("\nServer listing on port",port)
s.listen(1)
connection, clientAddress = s.accept()
filez = connection.recv(1024)
f = open(filez, "rb")
content = f.read()
connection.send(content)
f.close()
