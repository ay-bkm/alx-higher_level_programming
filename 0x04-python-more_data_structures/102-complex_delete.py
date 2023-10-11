#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        delt = []
        for q, p in a_dictionary.items():
            if p == value:
                delt.append(q)
        if delt != []:
            length = len(delt)
            i = 0
            while length > 0:
                a_dictionary.pop(delt[i])
                i += 1
                length -= 1
        return a_dictionary
