import socket
import time
import datetime

class Agent():

    IP = None
    Port = None

    s = None
    data = None
    
    Code = None
    Status = None
    X = None
    Y = None
    Z = None
    Hp = None
    MaxHp = None
    Name = None
    Dm = None
    XpLevel = None

    def Connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('127.0.0.1', 6667))

    def Send(self, datas):
        self.s.send(bytes(datas + "\n","utf-8"))

    def Run(self):
        while(True):
            data = self.s.recv(1024)
            print(data)
            self.Send("RE")

    def DataString(self):
        dataTemplate = None

        if(self.Status == 0):
            return "Main menu"
        elif(self.Status == 1):
            dataTemplate = "Name:\n{}\n \nPosition: \nX: {} \nY: {} \nZ: {} \n\nHealth: \n{} / {}"

            return dataTemplate.format(self.Name, self.X, self.Y, self.Z, self.Hp, self.MaxHp)
