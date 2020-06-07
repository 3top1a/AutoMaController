#!/usr/bin/env python

import os

import Agent  # Local libraries
import GUI

__author__ = "3top1a"
__license__ = "MIT"
__status__ = "Development"


class Main:
    Agents = []

    a = None

    def __init__(self):
        # The program starts here
        self.a = Agent.Agent()

        gui = GUI.GUI(self)

        self.a.connect()
        self.a.send_data_req()
        self.a.run()


try:
    main = Main()
except KeyboardInterrupt:
    print("\nInterrupted")
    os._exit(os.EX_OK)
