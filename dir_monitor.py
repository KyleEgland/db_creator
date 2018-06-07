#! python3
# This program will monitor a specified directory for changes.
import os
import re
import logging
import sys


##########
# Logger #
##########
# Setting up a separate logger to avoid using "root" logger
logger = logging.getLogger(__name__)
# Log level set
logger.setLevel(logging.DEBUG)

# Establishing log line format
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

# Establishing log file/directory
file_handler = logging.FileHandler('logs/dir_monitor.log')
# Adding formatter to file handler
file_handler.setFormatter(formatter)
# Separately setting log level for the file handler - just because
file_handler.setLevel(logging.DEBUG)

# Add the file handler to the logger
logger.addHandler(file_handler)
# --------------------------------------------------------------------------- #
#                                END SECTION                                  #
# --------------------------------------------------------------------------- #


#############
# Functions #
#############
# Return a list of a directory contents (including sub-directory names) to the
# caller.
def list_dir(path):
    try:
        # Instantiate a list to contain the new values for file names.
        dir_list = os.listdir(path)

        # Send the list back to the caller
        return dir_list
    except Exception as e:
        logger.critical('ERROR func "list_dir": {}'.format(e))
        sys.exit(0)


# Add full path to a file name to create an absolute path
def add_path(contents_list):
    # Create a list using list comprehension that will intake a list of names,
    # file or directory, and append it to the full path
    response_list = list(map(lambda x: os.path.abspath(x), contents_list))

    # Return the newly created list to the caller
    return response_list


# Remove directories from the input list in order to return a list of only
# files
def filter_dir(full_dir_list):
    # Use list comprehension to create a list from an input list by filtering
    # out the directories.
    response_list = list(filter(lambda x: os.path.isfile(x), full_dir_list))
    return response_list


# Filter out files from the directory filtered list that should not be used
def filter_files(file_list):
    # Regular expression for checking file name validity on first pass
    initial_check = re.compile(r'BOOMS|LIGHTS|ORIS|MB51')
    filtered_files = list(filter(lambda x: initial_check.search(x)))

    return filtered_files


# Remove the full path from a list containing files with absolute paths in
# order to return a list of file names only.
def remove_dir(dir_list):
    response_list = list(map(lambda x: os.path.basename(x), dir_list))

    return response_list


# Consolidation of add_path, filter_dir, and list_dir
def defineList(path):
    # Create a list of the file contents of the directory
    dir_files = list_dir(path)

    # Add the full path to each item in the list
    full_dir = add_path(dir_files)

    # Filter the directories out of the list
    filtered_dir = filter_dir(full_dir)

    return filtered_dir


if __name__ == '__main__':
    raw_info = defineList()
