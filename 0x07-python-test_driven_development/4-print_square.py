#!/usr/bin/python3
"""This prints a square with '#'"""


def print_square(size):
    """
    Prints a square with #

    Args:
        size (int): the value of width & height
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        print()

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
