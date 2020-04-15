import socket
import threading


class Agent:
    IP = "127.0.0.1"
    Port = 6667

    s = socket()

    PositionX = None
    PositionY = None
    PositionZ = None

    def start():
        s.bind((IP, Port))
        s.listen()
    
    def stop():
        pass
    
    def run():
        conn, addr = s.accept()
        while(true):
            data = conn.recv(1024)
            if not data:
                break
            ParseData(data)
    
    def ParseData(data):
        pass



class AgentManager:
    Agents = []


def connect(ip, port):
    x = Agent()
    x.IP = ip
    x.Port = port

    AgentManager.Agents.append(x)


def run():
    pass

