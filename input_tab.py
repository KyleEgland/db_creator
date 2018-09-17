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
        tk.Grid.rowconfigure(self, 2, weight=0)
        tk.Grid.rowconfigure(self, 3, weight=0)

        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)

        # ------------------- #
        # ROW 0 - File Select #
        # ------------------- #
        self.file_lbl = tk.Label(self, text='File select:')
        self.file_lbl.grid(row=0, column=0, sticky='sne', padx=5, pady=5)

        self.file_entry = tk.Entry(self)
        self.file_entry.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

        self.file_btn = ttk.Button(self, text='Browse')
        self.file_btn.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)

        # ----------------- #
        # Row 1 - DB Status #
        # ----------------- #
        self.db_status_lbl = tk.Label(self, text='DB Status:')
        self.db_status_lbl.grid(row=1, column=0, sticky='sne', padx=5, pady=5)

        self.db_status_var = tk.StringVar()

        self.db_status_out = tk.Label(self, textvariable=self.db_status_var)
        self.db_status_out.grid(row=1, column=1, sticky='nes', padx=5, pady=5)

        # --------------------------- #
        # Row 2 - Sample Output Frame #
        # --------------------------- #
        self.output_frame = ttk.Labelframe(self, text='Sample Output Data')
        self.output_frame.grid(row=2, column=0, columnspan=3)

        tk.Grid.rowconfigure(self.output_frame, 0, weight=0)
        tk.Grid.rowconfigure(self.output_frame, 1, weight=0)

        tk.Grid.columnconfigure(self.output_frame, 0, weight=1)
        tk.Grid.columnconfigure(self.output_frame, 1, weight=1)

        self.col_avail_lbl = tk.Label(self.output_frame,
                                      text='Columns Available')
        self.col_avail_lbl.grid(row=0, column=0, sticky='esw', padx=3, pady=3)

        self.hdr_slct_var = tk.StringVar()
        self.hdr_slct_box = tk.Listbox(self.output_frame,
                                       listvariable=self.hdr_slct_var)
        self.hdr_slct_box.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

        self.col_data_lbl = tk.Label(self.output_frame,
                                     text='Sample Col. Data')
        self.col_data_lbl.grid(row=0, column=1, sticky='esw', padx=3, pady=3)

        self.col_data_var = tk.StringVar()
        self.col_data_out = tk.Listbox(self.output_frame,
                                       listvariable=self.col_data_var)
        self.col_data_out.grid(row=1, column=1, sticky='nsew', padx=3, pady=3)

    def input_data(self):
        # Function to open file dialog to select input file
        pass
