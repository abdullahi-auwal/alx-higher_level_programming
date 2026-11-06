#!/usr/bin/python3
"""Square module.

Attributes:
    size (int): size of the square.
"""


class Square:
    """Represent a square.

    Attributes:
        size (int): size of the square.
    """
    def __init__(self, size):
        """Initialize Square instance.

        Args:
            size (int): the size of the square.
        """
        self.__size = size
