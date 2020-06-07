import tkinter as tk


class HistoryTab(tk.Frame):
    def __init__(self, parent, command, main):
        tk.Frame.__init__(self, parent, bg="red")
        self.label = tk.Label(self, text=command, anchor="w")
        self.label.pack(side="left", fill="both", expand=True)

        def click_cb():
            main.send_specific(command)

        self.button = tk.Button(self, text="send again", command=click_cb, anchor="s")
        self.button.pack(side="right", fill="both", expand=True)
