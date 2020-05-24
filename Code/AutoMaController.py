#!/usr/bin/env python

import Agent #Local libraries

__author__ = "3top1a"
__license__ = "MIT"
__status__ = "Development"

class Main():

    Agents = []

    def __init__(self):
        #The program starts here

        a = Agent.Agent()
        
        a.Connect()

        a.Run()


main = Main()