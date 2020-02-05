import socket as s

try:
    S = s.socket()
    S.connect(("localhost", 5252))
    filename = input("Enter file name :")
    S.send(filename.encode())
    content = S.recv(1024)
    print(content.decode())
except Exception as e:
    print(e)
