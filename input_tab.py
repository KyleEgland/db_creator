#! python3
#
# Input tab for Analyst program
# Import information:
# tkinter = GUI module, used to construt the GUI
# ttk = tkinter styling, more GUI stuff
import tkinter as tk
import tkinter.ttk as ttk


class InputTab(tk.Frame):
    # Initialization function
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # The "rowconfigure" and "columnconfigure"
        tk.Grid.rowconfigure(self, 0, weight=0)
        tk.Grid.rowconfigure(self, 1, weight=0)

        tk.Grid.columnconfigure(self, 0, weight=0)
        tk.Grid.columnconfigure(self, 1, weight=3)
        tk.Grid.columnconfigure(self, 2, weight=0)

        # ------------------- #
        # ROW 0 - File Select #
        # ------------------- #
        self.file_lbl = tk.Label(self, text='File select:')
        self.file_lbl.grid(row=0, column=0, sticky='sne', padx=5, pady=5)

        self.file_entry = tk.Entry(self)
        self.file_entry.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

        self.file_btn = ttk.Button(self, text='Browse')
        self.file_btn.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)

        # ------------------ #
        # Row 1 - Selections #
        # ------------------ #
        self.hdr_slct_var = tk.StringVar()
        self.hdr_slct_box = tk.Listbox(self, listvariable=self.hdr_slct_var)
        self.hdr_slct_box.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
