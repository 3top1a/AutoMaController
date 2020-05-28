import threading
import tkinter as tk
import tkinter.ttk


class GUI(threading.Thread):

    root = None

    def __init__(self):
        super().__init__()
        gui_thread = threading.Thread(target=self.run)
        gui_thread.start()

    def run(self):
        print("Started GUI")

        # Setup the window
        self.root = tk.Tk()

        self.root.mainloop()
