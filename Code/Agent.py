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


                X = data[1] #[1] = x
                Y = data[2] #[2] = y
                Z = data[3] #[3] = z
                Hp = data[4] #[4] = hp
                MaxHp = data[5] #[5] = max hp
                Name = data[6] #[6] = name
                Dm = data[7] #[7] = dimension
                XpLevel = data[8] #[8] = exp level

                btr_data = ( Name + " -- Position X: " + X + " Y: " + Y + " Z: " + Z + " in dimension " + Dm + "  Health: " + Hp + "/" + MaxHp + " exp level: " + XpLevel)


                command = "goto"

                s.send(command.encode())

                print(btr_data)
