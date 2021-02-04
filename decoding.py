#!/usr/bin/python
# -*- coding: UTF-8 -*-

def decoding_func(string, alphabet, key):
    alphabet_encod = alphabet[key:] + alphabet[:key]
    str_out = ''
    for i in string:
        if i.lower() not in alphabet:
            str_out += i
        else:
            if i.isupper():
                ch = alphabet_encod.index(i.lower())
                str_out += str(alphabet[ch]).upper()
            else:
                ch = alphabet_encod.index(i.lower())
                str_out += str(alphabet[ch])
    print(str_out)
