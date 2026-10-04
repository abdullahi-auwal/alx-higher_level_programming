#!/usr/bin/python3
def roman_to_int(roman_string):
    int_eq = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if not isinstance(roman_string, str):
        return 0

    overall = 0
    lenght = len(roman_string)

    for i in range(lenght):
        current = int_eq.get(roman_string[i], 0)
        if i + 1 < lenght and current < int_eq.get(roman_string[i + 1], 0):
            overall -= current
        else:
            overall += current
    return overall
