#! python3
# This program will monitor a specified directory for changes.
import os
import datetime
import getpass
import re
import logging


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

######################
# Global Variable(s) #
######################
user_name = getpass.getuser()
path_to_watch = 'C:\\Users\\{}\\Documents\\test_dir'.format(user_name)
dump_path = 'C:\\Users\\{}\\Documents\\test_dir\\misc'.format(user_name)
logger.debug('Watching {}'.format(path_to_watch))

# Regular expression for checking file name validity on first pass
initial_check = re.compile(r'BOOMS|LIGHTS|ORIS|MB51')


# Loop through items in directory, ignoring other directories
def ListDir(path):

    # Instantiate a list to contain the new values for file names
    dir_list = []

    # Loop through the names in the specified directory
    for fname in os.listdir(path):
        # Create an absolute path for the given name
        check = os.path.join(path, fname)
        # Check the absolute path to see if the given name is a directory
        if os.path.isdir(check):
            # If the name is a directory, skip it
            continue
        else:
            # If the name is a file, add it to the list
            dir_list.append(fname)

    return dir_list


# Get the contents of the globally specified directory
def defineList():
    # Use the path variable
    global path_to_watch
    global dump_path

    # Create a list of the file contents of the directory
    dir_files = ListDir(path_to_watch)
    # Create string of list for log entry
    log_str = ', '.join(dir_files)
    logger.info('Found {} files: {}'.format(len(dir_files), log_str))

    # Itterate over a copy of the list, "list(dir_files", remove unwanted files
    # from the dir and remove from list.
    for item in list(dir_files):
        search_name = initial_check.search(item)

        if search_name is not None:
            logger.info('{} is valid'.format(item))
        elif search_name is None:
            logger.info('{} is NOT valid'.format(item))
            # Create an absolute path of where the "bad" file is
            abs_path = os.path.join(path_to_watch, item)
            # Create an absolute path to move the "bad" file to
            new_path = os.path.join(dump_path, item)
            # Move the "bad" file
            os.rename(abs_path, new_path)
            dir_files.remove(item)

    return dir_files


# Loop through the list of files and add them to the dictionary
def prepDict(file_list):
    # Instantiate a dictionary to hold the key/value pairs created
    tmp_dict = {}

    # Get the current date and time
    currentTime = datetime.datetime.now()
    # Format the current date and time for use as a value in dict
    formattedTime = currentTime.strftime('%d-%b-%Y')

    # TODO:  Add in steps to handle a check against the database to ensure
    #        files aren't added more than once

    # Loop through the list to add file names and dates/times to dictionary
    for item in file_list:
        tmp_dict[item] = formattedTime
        print('Added file: {}'.format(item))


# Loop the program to keep polling the specified directory
# while True:
#
#     defineList()
#
#     time.sleep(10)
if __name__ == '__main__':
    raw_info = defineList()
    prepDict(raw_info)
