import socket
import time
import datetime
import threading

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

    def SendTheDataReq(self):
        threading.Timer(0.1, self.SendTheDataReq).start()
        self.Send("106")

    def Run(self):
        while(True):
            data = str( self.s.recv(1024) )

            data = data.split(' ')

            """ To communicate we use a bunch of prefixes
            pf. val | Who sends it (we are the client) | a description

            105 - S - Just testing the connection se that we can insult each other.
            105 - S - Sent every 2 seconds since out.checkError() can only return true if it sends data
            106 - C - Send me the data
            107 - S - (Response to 106) Here's the data you faggot
            108 - S - (Response to 106) We're in the main menu retard
            """
            
            pfx = data[1]
            print(pfx)
    
    def DataString(self):
        dataTemplate = None

        if(self.Status == 0):
            return "Main menu"
        elif(self.Status == 1):
            dataTemplate = "Name:\n{}\n \nPosition: \nX: {} \nY: {} \nZ: {} \n\nHealth: \n{} / {}"

            return dataTemplate.format(self.Name, self.X, self.Y, self.Z, self.Hp, self.MaxHp)
