#!/usr/bin/python3
def value_to_add(a, b, int_eq):
    va = int_eq[a]
    vb = int_eq[b]

    if va < vb:
        value = vb - va
    else:
        value = vb + va
    return value

def roman_to_int(roman_string):
    int_eq = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if roman_string == None:
        return 0
    if type(roman_string) != str:
        return 0
    
    ln = len(roman_string) - 1
    if ln == 0:
        return int_eq[roman_string]
    overall = 0
    n = 0
    while n <= ln:
        if n == ln:
            va = int_eq[roman_string[n]]
            overall = overall + va
            return overall
        this_val = value_to_add(roman_string[n], roman_string[n + 1], int_eq)
        overall = overall + this_val
        n = n + 2
    return overall
