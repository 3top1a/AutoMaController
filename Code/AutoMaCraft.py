import GUI as gui

import tkinter as tk
import tkinter.ttk


class Main():

    Agents = []

    def RunAgents(self):
        for i in self.Agents:
            RunIndAgent(i)

    def __init__(self):
        

        GUI = gui.GUI(self)

        while(1):
            RunAgents()
    
    def RunIndAgent(self, ag):
        pass



main = Main()