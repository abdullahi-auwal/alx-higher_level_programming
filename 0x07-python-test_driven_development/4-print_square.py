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
        raise ValueError("size must be >= 0")
    if size == 0:
        pass
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
