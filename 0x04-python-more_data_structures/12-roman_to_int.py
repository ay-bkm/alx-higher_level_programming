#!/usr/bin/python3
def to_subtract(list_num):
    sub = 0
    maximum_list = max(list_num)

    for n in list_num:
        if maximum_list > n:
            sub += n

    return (maximum_list - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for lf in roman_string:
        for r_num in list_keys:
            if r_num == lf:
                if rom_n.get(lf) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [rom_n.get(lf)]
                else:
                    list_num.append(rom_n.get(lf))

                last_rom = rom_n.get(lf)

    num += to_subtract(list_num)

    return (num)
