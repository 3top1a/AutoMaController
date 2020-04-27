import GUI as gui
import Agent as agent

import tkinter as tk
import tkinter.ttk


class Main():

    Agents = []

    def RunAgents(self):
        for i in self.Agents:
            i.Run()

    def __init__(self):

        a = agent.Agent()
        a.IP = "127.0.0.1"
        a.Port = 6667

        self.Agents.append(a)

        GUI = gui.GUI(self)

        while(1):
            GUI.ChangeDatalabel( self.Agents[0].DataString() )
            self.RunAgents()



main = Main()