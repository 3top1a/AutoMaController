import socket
import threading


class Agent:
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

    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('127.0.0.1', 6667))

    def send(self, msg):
        self.s.send(bytes(msg + "\n", "utf-8"))

    def send_data_req(self):
        threading.Timer(0.1, self.send_data_req).start()
        self.send("106")

    def run(self):
        while True:
            data = str(self.s.recv(1024))

            data = data.split(' ')

            """ To communicate we use a bunch of prefixes
            pf. val | Who sends it (we are the client) | a description

            105 - S - Just testing the connection se that we can insult each other.
            105 - S - Sent every 2 seconds since out.checkError() can only return true if it sends data
            106 - C - Send me the data
            107 - S - (Response to 106) Here's the data you faggot
            108 - S - (Response to 106) We're in the main menu retard
            109 - S - We just executed the command with {x} prefix (110, etc..)
            110 - C - Send this in the local chat you pillock
            """

            pfx = data[1]

            # Parsing based on the prefix

            if pfx == "105":
                # Nothing
                pass
            if pfx == "107":
                self.Status = 1

                self.X = str(data[2])  # [2] = x
                self.Y = str(data[3])  # [3] = y
                self.Z = str(data[4])  # [4] = z
                self.Hp = str(data[5])  # [5] = hp
                self.MaxHp = str(data[6])  # [6] = max hp
                self.Name = str(data[7])  # [7] = name
                self.Dm = str(data[8])  # [8] = dimension
                self.XpLevel = str(data[9])  # [9] = exp level

                # print(self.data_string())

            if pfx == "108":
                self.Status = 0

                # print("We are in the main menu")

    def data_string(self):
        if self.Status == 0:
            return "Main menu"
        elif self.Status == 1:
            data_template = "Name:\n{}\n \nPosition: \nX: {} \nY: {} \nZ: {} \n\nHealth: \n{} / {}"

            return data_template.format(self.Name, self.X, self.Y, self.Z, self.Hp, self.MaxHp)
