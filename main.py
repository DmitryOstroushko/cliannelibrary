# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from cliannelibrary.cliannelibrary import FileLibrary

if __name__ == '__main__':

    FileLibrary("/home/clianne/ФОТО/").rename_file_by_mask(False, '*', 20210300)

