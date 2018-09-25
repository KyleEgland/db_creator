#! python3
# This file provides the different structures for the data to be manipulated
# by the analyst.py program
import pandas as pd
import os
import sys
import logging


# ------------ #
# Logger Setup #
# ------------ #
# Check for the existence of a 'logs' folder - should one not exist, create it
if os.path.exists('./logs/'):
    pass
else:
    try:
        os.mkdir('./logs/')
    except Exception as e:
        print('[-] Unable to create directory - please check permissions')
        sys.exit()

# Log levels (low-high): Debug -> Info -> Warning -> Error -> Critical
# Instantiate a logger - instead of using root - to allow files to log
# independently (if there are multiple files in a project)
logger = logging.getLogger(__name__)

# This establishes what level to log (ref. log levels above)
logger.setLevel(logging.DEBUG)

# Format the string that prepends the information that goes into the log file
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                              datefmt='%d-%b-%Y %H')

# Create/name the log file
file_handler = logging.FileHandler('./logs/{}.log'.format(__name__))

# Link the specified format above to the logger
file_handler.setFormatter(formatter)

# Capture only Errors and above in file handler - this overrides ".setLevel"
# for the file
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
# NOTES:
# use logger.exception() to get the traceback in addtion to log message

# ---------- #
# End Logger #
# ---------- #


class InputData():
    # Class for holding data used accross multiple tabs in the analyst.py
    # program.  This class is specifically for use with data coming in (I.e.
    # the imported file, tentative data - data frame, etc.)
    def __init__(self, *args, **kwargs):
        # The absolute path to the file being accessed - takes in a file object
        # created by the filedialog.askopenfile() method
        self._file_name = ''
        # A list for all of the variables that need updates on the file name
        self._file_subs = []

        # The data from the file being accessed
        self._data_frame = ''
        # A list for the variables that need data frame info
        self._data_subs = []

        # Column names (gathered from self._data_frame)
        self._col_names = ''
        # List for variables that need column names
        self._col_subs = []

        # A pull from self._data_frame of user specified data (see
        # input_tab.py)
        self._sample_data = ''
        # List for variables that need sample data
        self._sample_subs = []

        self._subs_dict = {'file': self._file_subs, 'data': self._data_subs,
                           'col': self._col_subs, 'sample': self._sample_subs}

    def set_file_name(self, path):
        # The caller is responsible for actually providing the absolute path to
        # the desired file (os object)
        self._file_name = path

        # The newly set file is logged
        logger.debug('New file name - {}'.format(self._file_name))

        # The subscribers are updated
        self.update_subs(self._file_subs,
                         os.path.basename(self._file_name.name))

        # The information is passed off in order to become a data frame and
        # ending this function (the data frame function takes over from here)
        self.set_data_frame()

    def get_file_name(self):
        return self._file_name

    def set_data_frame(self):
        # Calling this is a result of there being a file selected, therefore
        # no arguments are needed and we process the info into a data frame
        self._data_frame = pd.read_csv(self._file_name.name)

        # The column information is then passed to the column variable
        self.set_col_names()

    def set_col_names(self):
        # Calling this is a result of there being a data frame, therefore no
        # arguments are needed - information processed in sequence
        self._col_names = self._data_frame.columns.values.tolist()

        # self._col_names = self._col_names.tolist()

        self.update_subs(self._col_subs, self._col_names)

    def set_sample_data(self, col, rows, direction):
        if direction == 'Top':
            self._sample_data = self._data_frame.iloc[0: int(rows),
                                                      int(col)].values.tolist()
        else:
            self._sample_data = self._data_frame.iloc[(-1 * int(rows)):,
                                                      int(col)].values.tolist()

        self.update_subs(self._sample_subs, self._sample_data)

    def drop_row(self, col, row_val):
        self._data_frame = self._data_frame[self._data_frame[col] != row_val]

    def add_sub(self, sub, sub_list):
        self._subs_dict[sub_list].append(sub)
        logger.debug('Added "{}" to "{}" subscriber list'.format(sub,
                                                                 sub_list))

    def update_subs(self, subs_list, var):
        for sub in subs_list:
            sub.set(var)
