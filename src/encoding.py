#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
A function that receives a string variable, a list, and a numeric key as input.
Encodes text by shifting the list with the original alphabet by 2 steps to the left.
"""


def encoding_func(string, alphabet, key):
    # Check the string for a valid value.
    for char in string.lower():
        if char.isalpha() and char not in alphabet:
            raise ValueError("The argument has an inappropriate value")
    # We get a new dictionary by shifting by a given step.
    alphabet_encode = alphabet[key:] + alphabet[:key]
    str_out = ""
    # We translate each letter of the string in accordance with the new encoding.
    for letter in string:
        if letter.lower() not in alphabet:
            str_out += letter
        else:
            ch = alphabet.index(letter.lower())
            if letter.isupper():
                str_out += str(alphabet_encode[ch]).upper()
            else:
                str_out += str(alphabet_encode[ch])
    return str_out


if __name__ == "__main__":
    pass
