#!/usr/bin/python3
"""Square module.

The square class provides functionality
for managing the size of a square and calculating its area
"""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize Square instance.

        Args:
            size (int, optional): the size of the square.
                default to 0
        """
        self.size = size

    def area(self):
        """calculate the area of the square.

        Returns:
            int: The area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """print in stdout the square
        with the character #.
        """
        if self.__size < 0:
            print()
        else:
            for i in self.__size:
                for j in self.__size:
                    print("#", end="")
                print()

    @property
    def size(self):
        """int: size of the square.

        Must be a non-negative integer.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
