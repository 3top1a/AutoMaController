import socket, time, re, multiprocessing

class Agent:

    Ip = ""
    Port = 6667

    Status = 0
    # 0 = main menu
    # 1 = in-game


    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("127.0.0.1", 6667))
            while(True):
                data = s.recv(1024)

                if not data:
                    break

                #parsing

                data = str(data).split(' ')

                if(len(data) < 2):
                    self.Status = 0
                    return
                else:
                    self.Status = 1

                Code = data[1] #[1] = Return code. 100 = SUCCESS : 101 = IN MAIN MENU

                if(Code == "100"):
                    X = data[2] #[2] = x
                    Y = data[3] #[3] = y
                    Z = data[4] #[4] = z
                    Hp = data[5] #[5] = hp
                    MaxHp = data[6] #[6] = max hp
                    Name = data[7] #[7] = name
                    Dm = data[8] #[8] = dimension
                    XpLevel = data[9] #[9] = exp level

                    btr_data = ( Name + " -- Position X: " + X + " Y: " + Y + " Z: " + Z + " in dimension " + Dm + "  Health: " + Hp + "/" + MaxHp + " exp level: " + XpLevel)
                    print(btr_data)
                else:
                    print("Main menu")


                #command = ". toggle freecam"

                #s.send(command.encode())