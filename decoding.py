key = -2


def decoding_func(string, alphabet, key):
    al = alphabet
    al_encod = al[key:] + al[:key]
    str_out = ''
    for i in string:
        if i not in al:
            str_out += i
        else:
            ch = al_encod.index(i.lower())
            str_out += str(al[ch])
    print(str_out)