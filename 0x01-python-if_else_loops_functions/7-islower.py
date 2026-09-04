#!/usr/bin/python3
def islower(c):
    equiv = ord(c)
    for i in range(97, 123):
        if (equiv == i):
            return (True)
    return (False)
