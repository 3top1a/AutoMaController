#!/usr/bin/env python

import Agent #Local libraries

import os

__author__ = "3top1a"
__license__ = "MIT"
__status__ = "Development"

class Main():

    Agents = []

    def __init__(self):
        #The program starts here

        a = Agent.Agent()
        
        a.Connect()
        a.SendTheDataReq()
        a.Run()



try:
    main = Main()
except KeyboardInterrupt:
    print("\nInterrupted")
    os._exit(os.EX_OK)