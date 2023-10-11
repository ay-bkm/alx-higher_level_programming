#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)

    score_l = 0
    weight_d = 0

    for tup in my_list:
        score_l += tup[0] * tup[1]
        weight_d += tup[1]

    return (score_l / weight_d)
