# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from cliannelibrary.filelibrary import FileLibrary


if __name__ == '__main__':

    path = sys.argv[1] # "/home/clianne/ФОТО/"
    FileLibrary().rename_file_by_mask(False, '*', 20210300)

