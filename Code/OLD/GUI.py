import tkinter as tk
import threading
import os

class GUI(threading.Thread):

    Main = None
    Style = None

    DataLabel = None
    LeftDataReadouts = None
    RightDataSending = None
    RightSendingPanel = None
    DataEntry = None
    DataSendButton = None
    LeftAreaFrame = None
    PacketFreqSlider = None
    LastPacketFreqSliderValue = None
    CommandSelectorFrame = None

    def __init__(self, _main):
        self.Main = _main
        threading.Thread.__init__(self)
        self.start()

    def QuitCallback(self):
        #Exit the app
        os._exit(os.EX_OK)
    
    def run(self):
        #Setup the window
        self.root = tk.Tk()
        #Set the title
        self.root.title("AutoMa Craft Controller")
        #Set the minimum size
        self.root.minsize(100, 100)
        #I dont know what this does, i copied this from stack overflow
        #Probably binds the close button to self.QuitCallback
        self.root.protocol("WM_DELETE_WINDOW", self.QuitCallback)
        #Set the app's theme
        #self.Style = tk.ttk.Style()
        #print(self.Style.theme_names())
        #Doesnt work on my pc for some reason
        #FIXME
        #self.Style.theme_use('alt')

        #Left frame
        self.LeftAreaFrame = tk.Frame(self.root, bg='blue', width=500)
        self.LeftAreaFrame.pack(expand=True, fill='both', side='left')

        #Left Data Readouts
        self.DataLabel = tk.Label(self.LeftAreaFrame, text="yeet", height="20", width="40", justify=tk.LEFT, anchor="nw")
        self.DataLabel.pack(expand=True, fill='both', side='left')

        #Data sending frame
        self.RightSendingPanel = tk.Frame(self.root, width=100, height=200)
        self.RightSendingPanel.pack(expand=True, fill='both', side='right')

        def set_pf(value):
            print(value)
            self.Main.Agents[0].send("103-" + value)

        def send():
            self.Main.Agents[0].send(self.DataEntry.get())        
        
        #Packet frequency slider
        self.PacketFreqSlider = tk.Scale(self.RightSendingPanel, from_=5, to=30, orient=tk.HORIZONTAL, length = 200, command=set_pf)
        #The packet sending shit doesnt really work rn due to the shitty socket server implementation
        #self.PacketFreqSlider.pack()
        
        #Command selector - frame

        self.CommandSelectorFrame = tk.Frame(self.RightSendingPanel, height=300, bg="red")
        self.CommandSelectorFrame.pack(expand=True, fill='both')

        #Command selector - buttons

        #Mode 1 - Chat (local)

        #Mode 2 - TODO
        
        
        #Button and entry
        self.DataEntry = tk.Entry(self.RightSendingPanel)
        self.DataEntry.insert(1, "sample")
        self.DataEntry.pack(expand=True, fill='x', side=tk.LEFT)
        
        self.DataSendButton = tk.Button(self.RightSendingPanel, text="Send", command = send)
        self.DataSendButton.pack(side=tk.RIGHT, pady=20)

        def update():
            to = str(self.Main.Agents[0].datastring())

            self.ChangeDatalabel(to)
            self.root.after(50, update)

        
        #Finalize
        self.PacketFreqSlider.set(5)
        self.root.after(50, update)
        self.root.mainloop()
    
    def ChangeDatalabel(self, text):
        if(self.DataLabel != None):
            self.DataLabel.config(text=text)