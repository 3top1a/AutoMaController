#!/usr/bin/env python

import tkinter as tk  #Standard libraries
import tkinter.ttk

import GUI as gui  #Local libraries
import Agent as agent



__author__ = "3top1a"
__license__ = "MIT"
__status__ = "Development"

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