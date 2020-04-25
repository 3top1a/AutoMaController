import GUI as gui
import Agent as agent
import Shell as shell

import subprocess, threading, multiprocessing

agents = []

def run():
    for i in agents:
        i.run()

def __init__():

    x = agent.Agent()
    x.IP = "localhost"
    x.Port = 6667
    agents.append(x)


    run()
    

__init__()
