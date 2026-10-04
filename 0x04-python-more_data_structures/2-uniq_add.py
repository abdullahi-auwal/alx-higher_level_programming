#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return 0
    _sum = 0
    uniq = set(my_list)
    for i in uniq:
        _sum = _sum + i
    return (_sum)
