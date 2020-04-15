import socket, time

class Agent:

    Ip = ""
    Port = 6667

    def run(shit):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((Ip, Port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(data)
