import os
import pickle
from os.path import exists

"""
Author: Yaly David
yalydav@gmail.com
3.9.22
"""


def new_file():
    """
    Creates a new document
    :return:
    """
    file_name = input("enter file name>>")
    file_text = input("enter your text >>")

    data = pickle.dumps(file_text)

    f = open(file_name, "wb")
    f.write(data)
    f.close()


def open_file(file_name):
    """
    Prints file's content
    :param file_name: path to file
    :return:
    """
    with open(file_name, "rb") as f:
        data = f.read()
        file_text = pickle.loads(data)
    print(f"{file_name}\n{file_text}")


def rm_file(file_name):
    """
    Removes a file
    :param file_name: path to file
    :return:
    """
    os.remove(file_name)


def main():
    while True:
        answer = input("1 for a new file\n"
                       "2 to open an existed file.\n"
                       "3 to delete a file\n"
                       ">>")
        if answer == "1":
            new_file()
        if answer == "2":
            file_name2 = input("what's the file's name?>>")
            if exists(file_name2):
                open_file(file_name2)
            else:
                print("you have tried to open a file that doesn't exist!")
        if answer == "3":
            remove_file = input("what file do you want to remove?>>")
            accept = input("are you sure you want to remove that file?>>")
            if accept == "yes":
                if exists(remove_file):
                    rm_file(remove_file)
                    print(f"{remove_file} was removed")
                else:
                    print("you have tried to remove a file that doesn't exist!")
            else:
                continue


if __name__ == '__main__':
    main()
