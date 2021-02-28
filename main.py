#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
from src.select_alphabet import select_alphabet
from src.decoding import decoding_func
from src.encoding import encoding_func

"""
The main file that runs the program logic.
The function of creating a command line parser is implemented here.
In the main () function, the received data is processed.
"""


def create_parser():
    # The function of creating a command line parser.
    parser = argparse.ArgumentParser(description="Process the string.")
    parser.add_argument("action", type=str, help="Choosing a function")
    parser.add_argument(
        "string",
        action="extend",
        nargs="+",
        type=str,
        help="Get a string for processing",
    )
    return parser


def main():
    # A function that contains the logic for processing input data.
    parser = create_parser()
    args = parser.parse_args()
    letter = args.string[0]
    param = vars(args)
    action = param.get("action")
    string = param.get("string")
    string = " ".join(string)
    alphabet = select_alphabet(letter[1])
    if action in ["e", "encoding"]:
        print(encoding_func(string, alphabet, -2))
    elif action in ["d", "decoding"]:
        print(decoding_func(string, alphabet, -2))
    else:
        print(f"{action} function does not exist")


if __name__ == "__main__":
    main()
