import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 6667))

while(True):
    data = s.recv(1024)
    print(data)
    s.send(b"REEEe" + b"\n")