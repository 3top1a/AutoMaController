import socket, time

class Agent:

    Ip = ""
    Port = 6667

    def run(shit):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("127.0.0.1", 6667))
            while(True):
                data = s.recv(4096)
                print(data)
