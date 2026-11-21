#!/usr/bin/python3
""" This module contains addition function."""


def add_integer(a, b=98):
    """ This function adds integers.

        Args:
            a (int, float): The first variable
            b (int, float): The second variable

        Returns:
            int: sum of the two variables
    """
    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
        else:
            a = int(a)

    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
        else:
            b = int(b)

    return a + b
