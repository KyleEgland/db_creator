#! python3
#
# Input tab for Analyst program
# Import information:
# tkinter = GUI module, used to construt the GUI
# ttk = tkinter styling, more GUI stuff
import tkinter as tk
import tkinter.ttk as ttk


class GraphTab(tk.Frame):
    # Initialization function
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # The "rowconfigure" and "columnconfigure"
        tk.Grid.rowconfigure(self, 0, weight=1)

        tk.Grid.columnconfigure(self, 0, weight=1)

        # ----- #
        # ROW 0 #
        # ----- #
        self.placeholder_lbl = tk.Label(self, text='Coming soon!')
        self.placeholder_lbl.grid(row=0, column=0, sticky='sne', padx=5,
                                  pady=5)
