#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if (j > i and j != i and i < 7 and j < 9):
            print("{}{}".format(i, j), end=", ")
print("79, 89")
