#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import os

"""
The module is designed to select the alphabet.
Based on the data received from the command line.
"""


def select_alphabet(string):
    # Checking for the validity of the input data type.
    if string is int:
        raise TypeError("The argument is of an invalid type.")
    files_list = []
    alphabet_list = []
    # We get a list of files from the data/
    for root, dirs, files in os.walk("./data"):
        for filename in files:
            files_list.append(filename)

    # We write the alphabet obtained from the file into the list.
    for filename_alphabet in files_list:
        alphabet_temp = []
        with open("data/" + filename_alphabet, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                alphabet_temp.extend(row)
        alphabet_list.append(alphabet_temp)

    # We define the alphabet with which we will work.
    for a_list in alphabet_list:
        if string[0].lower() in a_list:
            return a_list


if __name__ == "__main__":
    pass
