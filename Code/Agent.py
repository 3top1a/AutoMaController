import socket, time, re

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
                data = s.recv(4096)

                if not data:
                    break

                #parsing

                data = str(data).split(' ')

                if(len(data) < 2):
                    self.Status = 0
                    return
                else:
                    self.Status = 1

                btr_data = ""

                btr_data += ("Position X: " + data[1] + " Y: " + data[2] + "Z:" + data[3])

                print(btr_data)