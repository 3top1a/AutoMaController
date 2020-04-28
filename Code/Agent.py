import socket
import time

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

    def Run(self):
        while(True):
            #self.data = ""
            self.data = self.s.recv(1024*500)
            self.data = str(self.data).split(' ')

            self.Code = self.data[1]

            if(self.Code == "100"):
                self.Status = 1

                self.X = self.data[2] #[2] = x
                self.Y = self.data[3] #[3] = y
                self.Z = self.data[4] #[4] = z
                self.Hp = self.data[5] #[5] = hp
                self.MaxHp = self.data[6] #[6] = max hp
                self.Name = self.data[7] #[7] = name
                self.Dm = self.data[8] #[8] = dimension
                self.XpLevel = self.data[9] #[9] = exp level

                #btr_data = ( Name + " -- Position X: " + X + " Y: " + Y + " Z: " + Z + " in dimension " + Dm + "  Health: " + Hp + "/" + MaxHp + " exp level: " + XpLevel)
                #print(btr_data)
            elif (self.Code == "101") :
                self.Status = 0
                print("Main menu")
            else:
                print("The data is fucked")

    def DataString(self):
        return "Position: \n X: " + str(self.X) + " \n Y: " + str(self.Y) + "\n Z: " + str(self.Z) 
