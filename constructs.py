#! python3
# This file provides the different structures for the data to be manipulated
# by the analyst.py program


class InputFile():
    def __init__(self, *args, **kwargs):
        self._file_name = ''
        self._file_dir = ''
        self._col_names = ''
        self._sample_data = ''

    def set_file_name(self, path):
        self._file_name = path

    def set_file_dir(self, dir):
        self._file_name = dir
