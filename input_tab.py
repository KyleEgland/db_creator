#! python3
#
# Input tab for Analyst program
# Import information:
# tkinter = GUI module, used to construt the GUI
# ttk = tkinter styling, more GUI stuff
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog as file
import os


class InputTab(tk.Frame):
    # Initialization function
    def __init__(self, parent, data_construct):
        # Set a variable for the instance of the data construct imported in the
        # main application file
        self.data_in = data_construct

        tk.Frame.__init__(self, parent)
        # The "rowconfigure" and "columnconfigure"
        tk.Grid.rowconfigure(self, 0, weight=0)
        tk.Grid.rowconfigure(self, 1, weight=0)
        tk.Grid.rowconfigure(self, 2, weight=0)

        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)

        # ------------------- #
        # ROW 0 - File Select #
        # ------------------- #
        self.file_lbl = tk.Label(self, text='File select:')
        self.file_lbl.grid(row=0, column=0, sticky='sne', padx=5, pady=5)

        self.file_var = tk.StringVar()
        self.data_in.add_sub(self.file_var, 'file')
        self.file_entry = tk.Entry(self, textvariable=self.file_var,
                                   state='readonly')
        self.file_entry.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

        self.file_btn = ttk.Button(self, text='Browse',
                                   command=self.input_data)
        self.file_btn.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)

        # ----------------- #
        # Row 1 - DB Status #
        # ----------------- #
        self.db_status_lbl = tk.Label(self, text='DB Status:')
        self.db_status_lbl.grid(row=1, column=0, sticky='sne', padx=5, pady=5)

        self.db_status_var = tk.StringVar()

        self.db_status_out = tk.Label(self, textvariable=self.db_status_var)
        self.db_status_out.grid(row=1, column=1, sticky='nes', padx=5, pady=5)

        # ---------------------------- #
        # Row 2 - Output Pruning Frame #
        # ---------------------------- #
        self.output_frame = ttk.Labelframe(self, text='Output Data')
        self.output_frame.grid(row=2, column=0, columnspan=3, sticky='nsew',
                               padx=3, pady=3)

        tk.Grid.rowconfigure(self.output_frame, 0, weight=0)
        tk.Grid.rowconfigure(self.output_frame, 1, weight=1)
        tk.Grid.rowconfigure(self.output_frame, 2, weight=0)
        tk.Grid.rowconfigure(self.output_frame, 3, weight=0)
        tk.Grid.rowconfigure(self.output_frame, 4, weight=0)

        tk.Grid.columnconfigure(self.output_frame, 0, weight=1)
        tk.Grid.columnconfigure(self.output_frame, 1, weight=0)
        tk.Grid.columnconfigure(self.output_frame, 2, weight=1)
        tk.Grid.columnconfigure(self.output_frame, 3, weight=0)

        # Column Select
        self.col_avail_lbl = tk.Label(self.output_frame,
                                      text='Columns Available')
        self.col_avail_lbl.grid(row=0, column=0, sticky='esw', padx=3, pady=3)

        self.col_slct_var = tk.StringVar()
        self.data_in.add_sub(self.col_slct_var, 'col')
        self.col_slct_scroll = tk.Scrollbar(self.output_frame,
                                            orient='vertical')
        self.col_slct_box = tk.Listbox(self.output_frame,
                                       listvariable=self.col_slct_var,
                                       yscrollcommand=self.col_slct_scroll.set)
        self.col_slct_scroll.config(command=self.col_slct_box.yview)
        self.col_slct_scroll.grid(row=1, column=1, sticky='ns')
        self.col_slct_box.grid(row=1, column=0, sticky='nsew', pady=5)

        # Output data
        self.col_data_lbl = tk.Label(self.output_frame,
                                     text='Sample Col. Data')
        self.col_data_lbl.grid(row=0, column=2, sticky='esw', padx=3, pady=3)

        self.col_data_var = tk.StringVar()
        self.col_data_out = tk.Listbox(self.output_frame,
                                       listvariable=self.col_data_var)
        self.col_data_out.grid(row=1, column=2, sticky='nsew', padx=3, pady=3)

        # Viewing options
        self.show_data_lbl = tk.Label(self.output_frame,
                                      text='Show data from:')
        self.show_data_lbl.grid(row=2, column=0, sticky='nes', padx=3, pady=3)

        self.show_data_var = tk.StringVar()
        self.show_data_bx = ttk.Combobox(self.output_frame,
                                         textvariable=self.show_data_var)
        self.show_data_bx.grid(row=2, column=2, sticky='ew', padx=3, pady=3)

        self.num_show_lbl = tk.Label(self.output_frame, text='Number of rows:')
        self.num_show_lbl.grid(row=3, column=0, sticky='nes', padx=3, pady=3)

        self.num_show_entry = tk.Entry(self.output_frame)
        self.num_show_entry.grid(row=3, column=2, sticky='w', padx=3, pady=3)

        # Remove Selected
        self.rmv_col_btn = ttk.Button(self.output_frame,
                                      text='Remove selected column')
        self.rmv_col_btn.grid(row=4, column=0, sticky='ew', padx=3, pady=3)

        self.rmv_row_btn = ttk.Button(self.output_frame,
                                      text='Remove selected row')
        self.rmv_row_btn.grid(row=4, column=2, sticky='ew', padx=3, pady=3)

    # ------------- #
    # Tab Functions #
    # ------------- #
    def input_data(self):
        # Function to open file dialog to select input file
        home = os.path.expanduser('~')
        import_file = file.askopenfile(initialdir=home,
                                       title='Select Data File',
                                       filetype=(('CSV File', ('.csv')),
                                                 ('All Files', '*.*')))
        self.data_in.set_file_name(import_file)

    def num_val(self):
        checker = self.num_show_entry.get()
        try:
            int(checker)
        except Exception as e:
            tk.messagebox.ok(message='Please use digits in "Number of Rows".')

    def get_sample(self):
        pass
