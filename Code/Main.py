import Agent as agent

import threading
import tkinter as tk
import tkinter.ttk


### SCRIPT STRUCTURE
## AGENT MANAGMENT
## GUI
## CODE THAT ACTUALLY RUNS



##AGENT MANAGMENT
agents = []

def RunAgent():
    for i in agents:
        i.run()

##GUI
def StartGUI():
    window = tk.Tk()
    SideLabelVar = tk.StringVar()
    window.title("AutoMa Craft Controller")
    window.minsize(150,150)

    #ADD AGENT BUTTON
    ConnectButton = tk.Button(window, text ="Connect", command = RunAgent)
    ConnectButton.pack()

    SideLabel = tk.Label(window, textvariable = SideLabelVar)
    SideLabel.pack()

    while(True):
        SideLabelVar.set(agents[0].X)
        window.update_idletasks()
    window.mainloop()


##CODE THAT ACTUALLY RUNS (and maybe works...)
def __init__():

    x = agent.Agent()
    x.IP = "localhost"
    x.Port = 6667
    agents.append(x)

    x = threading.Thread(target=StartGUI, args=())
    x.start()

    RunAgent()

__init__()
