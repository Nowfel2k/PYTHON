import socket as s

try:
    S = s.socket()
    S.connect(("localhost", 4000))
    message = S.recv(100)
    while message:
        print("Received : ", message.decode())
        message = S.recv(100)
    S.close()

except Exception as e:
    print(e)
