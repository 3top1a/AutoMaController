import GUI as gui
import Classes as classes


def __init__():
    while(True):
        i = input("$ ")

        if(i.startswith("connect")):
            ip = i.split(' ')[1]
            port = i.split(' ')[2]

            print("Connecting to " + ip + " at port " + port)
            
            classes.connect(ip, port)
        if i.startswith("agents"):
            print("We have " + str(len(classes.AgentManager.Agents)))

__init__()