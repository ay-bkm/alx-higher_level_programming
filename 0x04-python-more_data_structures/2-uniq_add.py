#!/usr/bin/python3
def uniq_add(my_list=[]):
    ls = set(my_list)
    sum = 0
    for item in ls:
        sum += item
    return sum
