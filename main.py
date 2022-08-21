# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import string
import sys
from cliannelibrary.filelibrary import FileLibrary


if __name__ == '__main__':

    path: string = sys.argv[1] # "/home/clianne/ФОТО/"
    start_number: int = 20210300
    FileLibrary().rename_file_by_mask(False, '*', start_number)

