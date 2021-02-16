#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
A function that receives a string variable, a list, and a numeric key as input.
Decodes text by shifting the list with the original alphabet by 2 steps to the right.
"""


def decoding_func(string, alphabet, key):
    alphabet_encode = alphabet[key:] + alphabet[:key]  # list offset
    str_out = ""
    for letter in string:
        if letter.lower() not in alphabet:
            str_out += letter
        else:
            ch = alphabet_encode.index(letter.lower())
            if letter.isupper():
                str_out += str(alphabet[ch]).upper()
            else:
                str_out += str(alphabet[ch])
    return str_out


if __name__ == "__main__":
    pass
