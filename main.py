#!/usr/bin/python
# -*- coding: UTF-8 -*-


from src.cipher import get_input, select_alphabet
from src.decoding import decoding_func
from src.encoding import encoding_func


if __name__ == "__main__":
    string = get_input()[0].get("string")
    string = " ".join(string)
    letter = get_input()[1]
    action = get_input()[0].get("action")
    alphabet = select_alphabet(letter)
    if action in ["e", "encoding"]:
        print(encoding_func(string, alphabet, key=-2))
    elif action in ["d", "decoding"]:
        print(decoding_func(string, alphabet, key=2))
    else:
        print(f"{action} function does not exist")
