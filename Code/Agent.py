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
        self.s.send(b"\n")

    def Run(self):
        while(True):
            data = self.s.recv(1024)
            data = str(data).split(' ')
            self.Code = data[1]

            if(self.Code == "100"):
                self.Status = 1

                self.X = str( data[2] ) #[2] = x
                self.Y = str( data[3] ) #[3] = y
                self.Z = str( data[4] ) #[4] = z
                self.Hp = str( data[5] ) #[5] = hp
                self.MaxHp = str( data[6] ) #[6] = max hp
                self.Name = str( data[7] ) #[7] = name
                self.Dm = str( data[8] ) #[8] = dimension
                self.XpLevel = str( data[9] ) #[9] = exp level

                btr_data = ( self.Name + " -- Position X: " + self.X + " Y: " + self.Y + " Z: " + self.Z + " in dimension " + self.Dm + "  Health: " + self.Hp + "/" + self.MaxHp + " exp level: " + self.XpLevel)
                print(btr_data)
            elif (self.Code == "101"):
                self.Status = 0
                print("Main menu")
            else:
                print("The data is fucked")
            
            #Wait before sending the "send data again please" packet
            time.sleep(1/5)
            self.s.send(b"110\n")


    def send(self, datas):
        self.s.send(bytes(datas + "\n","utf-8"))

    def DataString(self):
        dataTemplate = None

        if(self.Status == 0):
            return "Main menu"
        elif(self.Status == 1):
            dataTemplate = "Name:\n{}\n \nPosition: \nX: {} \nY: {} \nZ: {} \n\nHealth: \n{} / {}"

            return dataTemplate.format(self.Name, self.X, self.Y, self.Z, self.Hp, self.MaxHp)
