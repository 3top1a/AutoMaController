import Agent as agent

import subprocess
import threading
import multiprocessing
import tkinter as tk
import tkinter.ttk


### SCRIPT STRUCTURE
## AGENT MANAGMENT
## GUI
## CODE THAT ACTUALLY RUNS


agents = []





def RunAgent():
    for i in agents:
        i.run()

def StartGUI():
    window = tk.Tk()
    window.title("M.A.C.C")
    window.minsize(150,150)

    #ADD AGENT BUTTON
    ConnectButton = tk.Button(window, text ="Connect", command = RunAgent)
    ConnectButton.pack()

    #TAB
    tab_parent = tkinter.ttk.Notebook(window)
    
    page1 = tkinter.ttk.Frame(tab_parent)
    tab_parent.add(page1, text='Tab1')

    window.mainloop()

def __init__():

    x = agent.Agent()
    x.IP = "localhost"
    x.Port = 6667
    agents.append(x)
    StartGUI()

__init__()
