#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}

    int_num = []
    for c in roman_string:
        for symbol in roman_num.keys():
            if c == symbol:
                int_num.append(roman_num.get(symbol))

    return sum(int_num)
