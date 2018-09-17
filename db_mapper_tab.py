#! python3
#
# Input tab for Analyst program
# Import information:
# tkinter = GUI module, used to construt the GUI
# ttk = tkinter styling, more GUI stuff
import tkinter as tk
import tkinter.ttk as ttk


class MapperTab(tk.Frame):
    # Initialization function
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # The "rowconfigure" and "columnconfigure"
        tk.Grid.rowconfigure(self, 0, weight=0)
        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.rowconfigure(self, 2, weight=1)

        tk.Grid.columnconfigure(self, 0, weight=1)

        # ------- #
        # DB Info #
        # ------- #
        self.db_info_frame = ttk.Labelframe(self, text='DB Info')
        self.db_info_frame.grid(row=0, column=0, sticky='nsew', padx=3, pady=3)

        tk.Grid.rowconfigure(self.db_info_frame, 0, weight=1)
        tk.Grid.rowconfigure(self.db_info_frame, 1, weight=1)

        tk.Grid.columnconfigure(self.db_info_frame, 0, weight=1)
        tk.Grid.columnconfigure(self.db_info_frame, 1, weight=1)

        self.db_status_lbl = tk.Label(self.db_info_frame, text='DB Status:')
        self.db_status_lbl.grid(row=0, column=0, sticky='nes', padx=3, pady=3)

        self.db_status_var = tk.StringVar()
        self.db_status_out = tk.Label(self.db_info_frame,
                                      textvariable=self.db_status_var)
        self.db_status_out.grid(row=0, column=1, sticky='nws', padx=3, pady=3)

        self.new_db_btn = ttk.Button(self.db_info_frame,
                                     text='New Local DB')
        self.new_db_btn.grid(row=1, column=0, sticky='ew', padx=3, pady=3)

        self.conn_existing_btn = ttk.Button(self.db_info_frame,
                                            text='Connect Existing DB')
        self.conn_existing_btn.grid(row=1, column=1, sticky='ew', padx=3,
                                    pady=3)

        # ---------- #
        # DB Options #
        # ---------- #
        self.db_options_frame = ttk.Labelframe(self, text='DB Options')
        self.db_options_frame.grid(row=1, column=0, sticky='nsew', padx=3,
                                   pady=3)

        tk.Grid.rowconfigure(self.db_options_frame, 0, weight=1)
        tk.Grid.rowconfigure(self.db_options_frame, 1, weight=1)

        tk.Grid.columnconfigure(self.db_options_frame, 0, weight=1)
        tk.Grid.columnconfigure(self.db_options_frame, 1, weight=1)
        tk.Grid.columnconfigure(self.db_options_frame, 2, weight=1)

        self.map_file_lbl = tk.Label(self.db_options_frame, text='Map File:')
        self.map_file_lbl.grid(row=0, column=0, sticky='nes', padx=3, pady=3)

        self.map_file_entry = tk.Entry(self.db_options_frame)
        self.map_file_entry.grid(row=0, column=1, sticky='ew', padx=3,
                                 pady=3)

        self.map_file_btn = ttk.Button(self.db_options_frame, text='Browse')
        self.map_file_btn.grid(row=0, column=2, sticky='ew', padx=3, pady=3)

        self.table_sel_lbl = tk.Label(self.db_options_frame, text='Table')
        self.table_sel_lbl.grid(row=1, column=0, sticky='nes', padx=3, pady=3)

        self.table_sel_var = tk.StringVar()
        self.table_sel_box = ttk.Combobox(self.db_options_frame,
                                          textvariable=self.table_sel_var)
        self.table_sel_box.grid(row=1, column=1, sticky='ew', padx=3, pady=3)

        self.table_add_btn = ttk.Button(self.db_options_frame,
                                        text='Add Table')
        self.table_add_btn.grid(row=1, column=2, sticky='ew', padx=3, pady=3)

        # -------------- #
        # Mapper Options #
        # -------------- #
        self.mapper_options_frame = ttk.Labelframe(self, text='Mapper Options')
        self.mapper_options_frame.grid(row=2, column=0, sticky='nsew', padx=3,
                                       pady=3)

        tk.Grid.rowconfigure(self.mapper_options_frame, 0, weight=1)
        tk.Grid.rowconfigure(self.mapper_options_frame, 1, weight=1)

        tk.Grid.columnconfigure(self.mapper_options_frame, 0, weight=1)
        tk.Grid.columnconfigure(self.mapper_options_frame, 1, weight=1)

        # Columns Available Widgets
        self.col_avail_lbl = tk.Label(self.mapper_options_frame,
                                      text='Columns Available')
        self.col_avail_lbl.grid(row=0, column=0, sticky='sew', padx=3, pady=3)

        self.col_avail_var = tk.StringVar()
        self.col_avail_box = tk.Listbox(self.mapper_options_frame,
                                        listvariable=self.col_avail_var)
        self.col_avail_box.grid(row=1, column=0, sticky='nsew', padx=3, pady=3)

        # Fields Available Widgets
        self.field_avail_lbl = tk.Label(self.mapper_options_frame,
                                        text='Fields Available')
        self.field_avail_lbl.grid(row=0, column=1, sticky='sew', padx=3,
                                  pady=3)

        self.field_avail_var = tk.StringVar()
        self.field_avail_box = tk.Listbox(self.mapper_options_frame,
                                          listvariable=self.field_avail_var)
        self.field_avail_box.grid(row=1, column=1, sticky='nsew', padx=3,
                                  pady=3)
