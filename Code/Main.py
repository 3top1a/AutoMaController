import GUI as gui
import Agent as agent
import Shell as shell

import subprocess
import threading
import multiprocessing 

agents = []

def run():
    for i in agents:
        i.run()

def __init__():

    x = agent.Agent()
    x.IP = "localhost"
    x.Port = 6667
    agents.append(x)


    while(True):
        Shell = shell.Prompt()
        Shell.prompt = "$"
        Shell.cmdloop('Starting prompt...')

        run()
        #shell()
    

__init__()
