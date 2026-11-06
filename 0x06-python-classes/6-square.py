#!/usr/bin/python3
"""Square module.

The square class provides functionality
for managing the size of a square and
calculating its area.
"""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square instance.

        Args:
            size (int, optional): the size of the square.
                default to 0
            position (tuple, optional): the position to start printing square
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square using using the #
        character.
        """
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
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

    @property
    def position(self):
        """tuple: position.

        Must tuple and size 2.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
