#!/usr/bin/python
# -*- coding: UTF-8 -*-

def encoding_func(string, alphabet, key):
    alphabet_encod = alphabet[key:] + alphabet[:key]
    str_out = ''
    for i in string:
        if i.lower() not in alphabet:
            str_out += i
        else:
            if i.isupper():
                ch = alphabet.index(i.lower())
                str_out += str(alphabet_encod[ch]).upper()
            else:
                ch = alphabet.index(i.lower())
                str_out += str(alphabet_encod[ch])
    print(str_out)
