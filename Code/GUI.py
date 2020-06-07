import ScrollableFrame
import HistoryTab

import threading
import os
import tkinter as tk


def quit_callback():
    os._exit(os.EX_OK)


class GUI(threading.Thread):

    Main = None
    root = None

    LeftAreaFrame = None
    DataLabel = None
    RightSendingPanel = None
    CommandSelectorFrame = None
    DataEntry = None
    DataSendButton = None
    HistoryTab = None

    def __init__(self, _main):
        self.Main = _main
        super().__init__()
        gui_thread = threading.Thread(target=self.run)
        gui_thread.start()

    # This function is just for the history tab
    def send_specific(self, command):
        self.Main.a.send("110 " + command)

    def run(self):
        print("Started GUI")

        # Setup the window
        self.root = tk.Tk()
        # Set the title
        self.root.title("AutoMa Craft Controller")
        # Set the minimum size
        self.root.minsize(100, 100)
        # Bind the close button to os._exit
        self.root.protocol("WM_DELETE_WINDOW", quit_callback)

        # The layout and widgets

        # Left frame
        self.LeftAreaFrame = tk.Frame(self.root, bg='blue', width=500)
        self.LeftAreaFrame.pack(expand=True, fill='both', side='left')

        # Left Data Readouts
        self.DataLabel = tk.Label(self.LeftAreaFrame, text="yeet", height="20", width="40", justify=tk.LEFT,
                                  anchor="nw")
        self.DataLabel.pack(expand=True, fill='both', side='left')

        # Data sending frame
        self.RightSendingPanel = tk.Frame(self.root, width=100, height=200)
        self.RightSendingPanel.pack(expand=True, fill='both', side='right')

        # History tab
        self.HistoryTab = ScrollableFrame.ScrollableFrame(self.RightSendingPanel, height=50)
        self.HistoryTab.pack(expand=False, fill='both')

        # Command selector - frame

        self.CommandSelectorFrame = tk.Frame(self.RightSendingPanel, height=150, bg="red")
        self.CommandSelectorFrame.pack(expand=True, fill='both')

        # Command selector - buttons

        # Mode 1 - Chat (local)
        # Mode 2 - TODO

        def send():
            # Mode 1
            self.Main.a.send("110 " + self.DataEntry.get())

            h = HistoryTab.HistoryTab(self.HistoryTab.scrollable_frame, self.DataEntry.get(), self)
            h.pack(side="top", expand=True)

        # Button and entry
        self.DataEntry = tk.Entry(self.RightSendingPanel)
        self.DataEntry.insert(1, "sample")
        self.DataEntry.pack(expand=True, fill='x', side=tk.LEFT)

        self.DataSendButton = tk.Button(self.RightSendingPanel, text="Send", command=send)
        self.DataSendButton.pack(side=tk.RIGHT, pady=20)

        # Finalize

        # Make an update loop
        def update():
            to = str(self.Main.a.data_string())
            self.DataLabel.config(text=to)
            self.root.after(50, update)
            self.HistoryTab.pack(expand=True, fill='both')

        # Integrate the update loop
        self.root.after(50, update)
        # Main loop
        self.root.mainloop()
