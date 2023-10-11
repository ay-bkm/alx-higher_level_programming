#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_key = list(a_dictionary.keys())
    ord_key.sort()
    for item in ord_key:
        print("{}: {}".format(item, a_dictionary.get(item)))
