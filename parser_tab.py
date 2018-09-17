#! python3
#
# Input tab for Analyst program
# Import information:
# tkinter = GUI module, used to construt the GUI
# ttk = tkinter styling, more GUI stuff
import tkinter as tk
import tkinter.ttk as ttk


class ParserTab(tk.Frame):
    # Initialization function
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # The "rowconfigure" and "columnconfigure"
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.rowconfigure(self, 2, weight=1)

        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)

        # -------------- #
        # ROW 0 - Output #
        # -------------- #
        self.out_select_lbl = tk.Label(self, text='Output Type')
        self.out_select_lbl.grid(row=0, column=0, sticky='sne', padx=5,
                                 pady=5)

        self.out_select_var = tk.StringVar()
        self.out_select_box = ttk.Combobox(self,
                                           textvariable=self.out_select_var)
        self.out_select_box.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

        # ----------------- #
        # ROW 1 - Add Group #
        # ----------------- #
        self.add_grp_lbl = tk.Label(self, text='Add Group:')
        self.add_grp_lbl.grid(row=1, column=0, sticky='sne', padx=5, pady=5)

        self.add_group_entry = tk.Entry(self)
        self.add_group_entry.grid(row=1, column=1, sticky='nsew', padx=5,
                                  pady=5)

        self.add_group_btn = ttk.Button(self, text='+')
        self.add_group_btn.grid(row=1, column=2, sticky='nsw', padx=5, pady=5)

        # ------------------------- #
        # ROW 2 - Edit Associations #
        # ------------------------- #
        self.assoc_frame = ttk.Labelframe(self, text='Edit Associations')
        self.assoc_frame.grid(row=2, column=0, columnspan=3, sticky='nsew',
                              padx=3, pady=3)

        tk.Grid.rowconfigure(self.assoc_frame, 0, weight=1)
        tk.Grid.rowconfigure(self.assoc_frame, 1, weight=1)

        tk.Grid.columnconfigure(self.assoc_frame, 0, weight=1)
        tk.Grid.columnconfigure(self.assoc_frame, 1, weight=1)
        tk.Grid.columnconfigure(self.assoc_frame, 2, weight=1)

        # Groups Widgets
        self.groups_lbl = tk.Label(self.assoc_frame, text='Groups:')
        self.groups_lbl.grid(row=0, column=0, sticky='sew', padx=3, pady=3)

        self.groups_var = tk.StringVar()
        self.groups_lst = tk.Listbox(self.assoc_frame,
                                     listvariable=self.groups_var)
        self.groups_lst.grid(row=1, column=0, sticky='nsew', padx=3, pady=3)

        # Target Field Widgets
        self.trgt_field_lbl = tk.Label(self.assoc_frame, text='Target Field')
        self.trgt_field_lbl.grid(row=0, column=1, sticky='sew', padx=3, pady=3)

        self.trgt_field_var = tk.StringVar()
        self.trgt_field_lst = tk.Listbox(self.assoc_frame,
                                         listvariable=self.trgt_field_var)
        self.trgt_field_lst.grid(row=1, column=1, sticky='nsew', padx=3,
                                 pady=3)

        # Word association
        self.assoc_lbl = tk.Label(self.assoc_frame, text='Word Association')
        self.assoc_lbl.grid(row=0, column=2, sticky='sew', padx=3, pady=3)

        self.assoc_var = tk.StringVar()
        self.assoc_lst = tk.Listbox(self.assoc_frame,
                                    listvariable=self.assoc_var)
        self.assoc_lst.grid(row=1, column=2, sticky='nsew', padx=3, pady=3)
