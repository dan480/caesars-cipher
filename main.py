#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import csv
import sys
from encoding import encoding_func, key
from decoding import decoding_func, key

alphabet = []

for root, dirs, files in os.walk("./data"):  
    for filename in files:
        print(filename)

with open('data/russian.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        alphabet.extend(row)


if __name__ == "__main__":
    if len (sys.argv) <= 2:
        print ("Missing parameters!")
        sys.exit(1)
    else:
        if len (sys.argv) > 3:
            print ("Error. Expected 1 parameter.")
            sys.exit(1)
            
        if len (sys.argv) == 3:
            param_name = sys.argv[1]
            param_string = sys.argv[2]         
            if (param_name == "encoding"):
                encoding_func(param_string, alphabet, key)
            elif (param_name == "decoding"):
                decoding_func(param_string, alphabet, key)
            else:
                print ("Error. Unknown parameter'{}'".format(param_name))
                sys.exit(1)

