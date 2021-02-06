#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
The code takes a string parameter.
Loads preset alphabets from a folder.
Determines which language the entered text belongs to.
Encodes / decodes text by shifting to the left by 2 steps.
Outputs the result
"""

import os
import csv
import sys
from src.encoding import encoding_func
from src.decoding import decoding_func

# Defining variables
key = -2
alphabet = []
alphabet_list = []
files_list = []

# Defining a variable to store the received text
text_input = sys.argv[2]

# We get a list of files from the data/
for root, dirs, files in os.walk("./data"):
    for filename in files:
        files_list.append(filename)

# We write the alphabet obtained from the file into the list.
for filename_alphabet in files_list:
    alphabet_temp = []
    with open("data/"+filename_alphabet, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            alphabet_temp.extend(row)
    alphabet_list.append(alphabet_temp)

# We define the alphabet with which we will work.
for a_list in alphabet_list:
    if text_input[0].lower() in a_list:
        alphabet = a_list
        break


def main():
    pass


# The program logic that determines the correspondence of the input parameters and runs the code.
if len(sys.argv) <= 2:
    print("Missing parameters!")
    sys.exit(1)
else:
    if len(sys.argv) > 3:
        print("Error. Expected 1 parameter.")
        sys.exit(1)
    elif len(sys.argv) == 3:
        param_name = sys.argv[1]
        param_string = sys.argv[2]
        if param_name in ["encoding", "-e"]:
            encoding_func(param_string, alphabet, key)
        elif param_name in ["decoding", "-d"]:
            decoding_func(param_string, alphabet, key)
        else:
            print("Error. Unknown parameter'{}'".format(param_name))
            sys.exit(1)

if __name__ == '__main__':
    main()
