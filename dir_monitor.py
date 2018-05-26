#! python3
# This program will monitor a specified directory for changes.
import os
import datetime


path_to_watch = 'C:\\Users\\kylee\\Documents\\test_dir'

# Instantiate global variable(s)
on_list = {}


def defineList():
    global on_list

    currentTime = datetime.datetime.now()
    formattedTime = currentTime.strftime('%d-%b-%Y')

    new_list = os.listdir(path_to_watch)
    for item in new_list:
        on_list[item] = formattedTime
    print(on_list)


defineList()

# while 1:
#     time.sleep(10)
#
#     new_list = dict([(f, None) for f in os.listdir(path_to_watch)])
#
#     added = [f for f in before if not f in after]
#
#     removed = [f for f in before if not f in after]
#
#     if added:
#         print('Added: {}'.format(added))
#
#     if removed:
#         print('Removed: {}'.format(removed))
#
#     before = after
