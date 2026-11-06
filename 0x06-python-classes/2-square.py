#!/usr/bin/python3
"""Square module.

Attributes:
    size (int, optional): size of the square.
"""


class Square:
    """Represent a square.

    Attributes:
        size (int, optional): size of the square.
    """
    def __init__(self, size=0):
        """Initialize Square instance.

        Args:
            size (int, optional): the size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must br >= 0")
        self.__size = size
