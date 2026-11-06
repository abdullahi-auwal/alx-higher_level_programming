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
        self.__size = size

    def area(self):
        """Returns the area of the square.

        Returns: area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Square getter property.

        Returns: the size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the square class"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
