#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import os
import argparse


def get_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", type=str)
    parser.add_argument("string", action="extend", nargs="+", type=str)
    args = parser.parse_args()
    letter = args.string[0]
    param = vars(args)
    return param, letter


def select_alphabet(string):
    files_list = []
    alphabet_list = []
    # We get a list of files from the data/
    for root, dirs, files in os.walk("./data"):
        for filename in files:
            files_list.append(filename)

    # We write the alphabet obtained from the file into the list.
    for filename_alphabet in files_list:
        alphabet_temp = []
        with open("data/" + filename_alphabet, newline="") as f:
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
