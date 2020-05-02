import tkinter as tk
import threading
import os

class GUI(threading.Thread):

    Main = None

    DataLabel = None

    def __init__(self, _main):
        self.Main = _main
        threading.Thread.__init__(self)
        self.start()

    def QuitCallback(self):
        os._exit(os.EX_OK)
    
    def run(self):
        self.root = tk.Tk()
        self.root.title("AutoMa Craft Controller")
        self.root.minsize(150, 150)
        self.root.protocol("WM_DELETE_WINDOW", self.QuitCallback)

        self.DataLabel = tk.Label(self.root, text="")
        self.DataLabel.config(anchor=tk.W)
        self.DataLabel.pack()

        def update():
            to = str( self.Main.Agents[0].DataString() )

            self.ChangeDatalabel(to)
            self.root.after(100, update)

        self.root.after(100, update)
        self.root.mainloop()
    
    def ChangeDatalabel(self, text):
        if(self.DataLabel != None):
            self.DataLabel.config(text=text)