#!/usr/bin/env python

import Agent #Local libraries
import GUI

import os
import threading

__author__ = "3top1a"
__license__ = "MIT"
__status__ = "Development"

class Main():

    Agents = []

    a = None

    def __init__(self):
        #The program starts here

        self.a = Agent.Agent()

        self.a.Connect()
        gui = GUI.GUI(self)
        self.a.SendTheDataReq()
        self.a.Run()



try:
    main = Main()
except KeyboardInterrupt:
    print("\nInterrupted")
    os._exit(os.EX_OK)