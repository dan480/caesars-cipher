#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
A function that receives a string variable, a list, and a numeric key as input.
Encodes text by shifting the list with the original alphabet by 2 steps to the left.
"""


def encoding_func(string, alphabet, key):
    alphabet_encode = alphabet[key:] + alphabet[:key]
    str_out = ''
    for letter in string:
        if letter.lower() not in alphabet:
            str_out += letter
        else:
            if letter.isupper():
                ch = alphabet.index(letter.lower())
                str_out += str(alphabet_encode[ch]).upper()
            else:
                ch = alphabet.index(letter.lower())
                str_out += str(alphabet_encode[ch])
    print(str_out)
