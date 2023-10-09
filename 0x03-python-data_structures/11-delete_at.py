#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    for item_i, item_v in enumerate(my_list):
        if item_i == idx:
            my_list.remove(item_v)
    return (my_list)
