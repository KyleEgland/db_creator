#! python3
#
# Input tab for Analyst program
# Import information:
# tkinter = GUI module, used to construt the GUI
# ttk = tkinter styling, more GUI stuff
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog as file
from tkinter import messagebox as mb
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

        # ------------- #
        # Column Select #
        # ------------- #
        self.col_avail_lbl = tk.Label(self.output_frame,
                                      text='Columns Available')
        self.col_avail_lbl.grid(row=0, column=0, sticky='esw', padx=3, pady=3)

        self.col_slct_var = tk.StringVar()
        # Subscribe to construct for columns
        self.data_in.add_sub(self.col_slct_var, 'col')
        # Scrollbar for column select listbox
        self.col_slct_scroll = tk.Scrollbar(self.output_frame,
                                            orient='vertical')
        self.col_slct_box = tk.Listbox(self.output_frame,
                                       listvariable=self.col_slct_var,
                                       yscrollcommand=self.col_slct_scroll.set,
                                       exportselection=False)
        self.col_slct_scroll.config(command=self.col_slct_box.yview)
        self.col_slct_box.bind('<<ListboxSelect>>', self.get_sample)
        self.col_slct_scroll.grid(row=1, column=1, sticky='ns')
        self.col_slct_box.grid(row=1, column=0, sticky='nsew', pady=5)
        # Creating a variable to contain the last selected item from the column
        # box so that it may be used elsewhere when the box loses focus (I.e. a
        # sample row is selected from the output box)
        # self.last_col = ''

        # ----------- #
        # Output data #
        # ----------- #
        self.col_data_lbl = tk.Label(self.output_frame,
                                     text='Sample Col. Data')
        self.col_data_lbl.grid(row=0, column=2, sticky='esw', padx=3, pady=3)

        self.col_data_var = tk.StringVar()
        # Subscribe to the sample data output from constructs
        self.data_in.add_sub(self.col_data_var, 'sample')
        # Scrollbar for output listbox
        self.col_data_scroll = tk.Scrollbar(self.output_frame,
                                            orient='vertical')
        self.col_data_out = tk.Listbox(self.output_frame,
                                       listvariable=self.col_data_var,
                                       yscrollcommand=self.col_data_scroll.set,
                                       exportselection=False)
        self.col_data_scroll.config(command=self.col_data_out.yview)
        self.col_data_scroll.grid(row=1, column=3, sticky='ns')
        self.col_data_out.grid(row=1, column=2, sticky='nsew', pady=3)

        # --------------- #
        # Viewing options #
        # --------------- #
        self.show_data_lbl = tk.Label(self.output_frame,
                                      text='Show data from:')
        self.show_data_lbl.grid(row=2, column=0, sticky='nes', padx=3, pady=3)

        self.dir_var = tk.StringVar()
        self.show_data_bx = ttk.Combobox(self.output_frame, justify='center',
                                         state='readonly',
                                         textvariable=self.dir_var,
                                         values=['Top', 'Bottom'])
        # Set default combobox value
        self.show_data_bx.current(0)
        self.dir_var.trace('w', self.requery)
        self.show_data_bx.grid(row=2, column=2, sticky='ew', padx=3, pady=3)

        self.num_show_lbl = tk.Label(self.output_frame, text='Number of rows:')
        self.num_show_lbl.grid(row=3, column=0, sticky='nes', padx=3, pady=3)

        self.num_show_entry = tk.Entry(self.output_frame)
        # Set default value for number of rows
        self.num_show_entry.insert(0, 10)
        self.num_show_entry.grid(row=3, column=2, sticky='w', padx=3, pady=3)

        # Remove Selected
        self.rmv_col_btn = ttk.Button(self.output_frame,
                                      text='Remove selected column',
                                      command=self.remove_column)
        self.rmv_col_btn.grid(row=4, column=0, sticky='ew', padx=3, pady=3)

        self.rmv_row_btn = ttk.Button(self.output_frame,
                                      text='Remove selected row',
                                      command=self.remove_row)
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
        if import_file is None:
            return None
        else:
            self.data_in.set_file_name(import_file)

    def num_val(self):
        # Function used to validate the contents of the entyr widget for the
        # number of sample rows desired
        try:
            # This ensures that the contents of the widget are a number
            checker = int(self.num_show_entry.get())
            # There is no point in returning 0 rows of sample data so we'll
            # catch it in case the user made a mistake
            if checker > 0:
                return checker
            else:
                mb.showinfo(title='More than 0',
                            message='Please input a number greater than 0',
                            icon='warning')
                return None

        except Exception as e:
            msg = 'Please use digits in "Number of Rows".'
            mb.showinfo(title='Missing/Erroneous Value', message=msg,
                        icon='warning',)
            return None

    def get_sample(self, evt):
        # The binding passes the widget to the function, this is handled below
        # by accepting it as a variable to be worked with
        selection = evt.widget

        # This try/except is being used because when the list box item is
        # 'unselected' the function is called again.  This causes errors which
        # are now handled via this try/except block.
        try:
            # self.last_col = selection.get(selection.curselection())
            col = selection.index(selection.curselection())
        except Exception as e:
            # A return used to exit the function without going further
            return None

        # Call the validation created previously to ensure that the appropriate
        # information is being processed
        rows = self.num_val()
        # Exit the function if there was an issue with the validation
        if rows is None:
            return None

        direction = self.show_data_bx.get()
        # Ensure that a direction was selected
        if direction != 'Top' and direction != 'Bottom':
            mb.showinfo(title='Select Direction',
                        message='Please make a direction selection.',
                        icon='warning')

        # Pass the information off to the constructs script to be acted upon
        self.data_in.set_sample_data(col, rows, direction)

    def requery(self, *args):
        try:
            col = self.col_slct_box.index(self.col_slct_box.curselection())
        except Exception as e:
            # TODO: Enter logging line
            return None
        rows = self.num_val()
        direction = self.show_data_bx.get()
        self.data_in.set_sample_data(col, rows, direction)

    def remove_row(self):
        # Use try/except to catch errors when button is pressed without data
        # loaded/selection(s) made
        try:
            col = self.col_slct_box.get(self.col_slct_box.curselection())
        except Exception as e:
            # TODO: logging statement
            return None

        # Get the name of the value in the undesired column
        try:
            row_val = self.col_data_out.get(self.col_data_out.curselection())
        except Exception as e:
            # TODO: logging statement needed
            return None

        self.data_in.drop_row(col, row_val)
        self.requery()

    def remove_column(self):
        try:
            col = self.col_slct_box.get(self.col_slct_box.curselection())
        except Exception as e:
            # TODO:  logging statement needed
            return None
        self.data_in.drop_col(col)
        self.requery()
