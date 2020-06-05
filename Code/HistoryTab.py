import tkinter as tk


class HistoryTab(tk.Frame):
    def __init__(self, parent, command, main):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text=command)
        self.label.pack(side="left", fill="both", expand=True)

        def click_cb():
            main.send_specific(command)

        self.button = tk.Button(self, text="send again", command=click_cb)
        self.button.pack(side="left", fill="both", expand=True)
