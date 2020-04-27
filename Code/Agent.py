import socket

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

    def Run(self):
        try:
            self.data = ""
            self.data = self.s.recv(1024)
            self.data = str(self.data).split(' ')
        except:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect(('localhost', 6667))

        try:
            self.Code = self.data[1] #[1] = Return code. 100 = SUCCESS : 101 = IN MAIN MENU

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
            else:
                self.Status = 0
                print("Main menu")
        except:
            print("error parsing")

    def DataString(self):
        return "Position: \n X: " + str(self.X) + " \n Y: " + str(self.Y) + "\n Z: " + str(self.Z) 
