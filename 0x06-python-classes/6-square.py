#!/usr/bin/python3
"""This module defines a class Square."""

class Square:
    """ This class represents a square with a given size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """ This method initializes the square object with a size and position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ This property gets the size value of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ This property sets the size value of the square.
        """
        if not isinstance(value, int):
            raise TypeError("The size must be an integer.")
        if value < 0:
            raise ValueError("The size must be a non-negative integer.")
        self.__size = value

    @property
    def position(self):
        """ This property gets the position value of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ This property sets the position value of the square.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("Position must be a tuple of 2 non-negative integers.")
        self.__position = value

    def area(self):
        """ This method calculates and returns the area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """ This method prints a square of '#' symbols according to the size and position values.
        """
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            print("\n".join(" " * self.position[0] + "#" * self.size for _ in range(self.size)))
