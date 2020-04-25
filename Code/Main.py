import GUI as gui
import Agent as agent

import subprocess, threading, multiprocessing, _thread
import tkinter as tk

agents = []

def StartWindow():
    window = tk.Tk()
    window.title("M.A.C.C")
    window.minsize(150,150)

    B = tk.Button(window, text ="Connect", command = RunAgent)
    B.pack()

    window.mainloop()

def RunAgent():
    for i in agents:
        i.run()

def __init__():

    x = agent.Agent()
    x.IP = "localhost"
    x.Port = 6667
    agents.append(x)


    StartWindow()

__init__()
