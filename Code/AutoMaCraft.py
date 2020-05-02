import GUI as gui
import Agent as agent

import tkinter as tk
import tkinter.ttk


class Main():

    Agents = []

    def RunAgents(self):
        #for i in self.Agents:
        pass

    def __init__(self):

        a = agent.Agent()

        self.Agents.append(a)

        GUI = gui.GUI(self)

        self.Agents[0].Connect()

        while(1):
            self.Agents[0].Run()



main = Main()