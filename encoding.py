key = -2


def encoding_func(string, alphabet, key):
    al = alphabet
    al_encod = al[key:] + al[:key]
    str_out = ''
    for i in string:
        if i not in al:
            str_out += i
        else:
            ch = al.index(i.lower())
            str_out += str(al_encod[ch])
    print(str_out)
