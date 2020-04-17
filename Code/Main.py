import GUI as gui
import Agent as agent

import subprocess
import threading

import multiprocessing 

agents = []

def shell():
    i = input("$ ")

    if(i.startswith("connect")):
        ip = i.split(' ')[1]
        port = i.split(' ')[2]

        print("Connecting to " + ip + " at port " + port)
        
        x = agent.Agent()
        x.IP = ip
        x.Port = port
        agents.append(x)
    
    if (i.startswith("agents")):
        print("We have " + str(len(agents)))

    if(i.startswith("exit")):
        exit()

def run():
    for i in agents:
        i.run()

def __init__():

    x = agent.Agent()
    x.IP = "localhost"
    x.Port = 6667
    agents.append(x)


    while(True):
        run()
        #shell()
    

__init__()
