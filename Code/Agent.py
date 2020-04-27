import socket

class Agent():

    IP = None
    Port = None
    
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
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.IP, self.Port))
            while(True):
                data = s.recv(1024)

                if not data:
                    break

                #parsing

                data = str(data).split(' ')

                Code = data[1] #[1] = Return code. 100 = SUCCESS : 101 = IN MAIN MENU

                if(Code == "100"):
                    self.Status = 1

                    self.X = data[2] #[2] = x
                    self.Y = data[3] #[3] = y
                    self.Z = data[4] #[4] = z
                    self.Hp = data[5] #[5] = hp
                    self.MaxHp = data[6] #[6] = max hp
                    self.Name = data[7] #[7] = name
                    self.Dm = data[8] #[8] = dimension
                    self.XpLevel = data[9] #[9] = exp level

                    #btr_data = ( Name + " -- Position X: " + X + " Y: " + Y + " Z: " + Z + " in dimension " + Dm + "  Health: " + Hp + "/" + MaxHp + " exp level: " + XpLevel)
                    #print(btr_data)
                else:
                    self.Status = 0
                    print("Main menu")

    def DataString(self):
        return "Position: \n X: " + str(self.X) + " \n Y: " + str(self.Y) + "\n Z: " + str(self.Z) 
