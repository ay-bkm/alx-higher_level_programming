#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """ This class represents a square with a given size.
    """

    def __eq__(self, other):
        """Defines the equality comparison to another Square."""
        return self.__size == other.__size

    def __lt__(self, other):
        """Defines the less-than comparison to another Square."""
        return self.__size < other.__size

    def __le__(self, other):
        """Defines the less-than-or-equal-to comparison to another Square."""
        return self.__size <= other.__size

    def __ne__(self, other):
        """Defines the inequality comparison to another Square."""
        return self.__size != other.__size

    def __gt__(self, other):
        """Defines the greater-than comparison to another Square."""
        return self.__size > other.__size

    def __ge__(self, other):
        """the greater-than-or-equal-to comparison to another Square."""
        return self.__size >= other.__size

    def __init__(self, size=0):
        """Initializes a new Square with a given size."""
        self.size = size

    def area(self):
        """Calculates and returns the area of the Square."""
        return (self.__size ** 2)

    @property
    def size(self):
        """Gets or sets the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the Square."""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        elif value < 0:
            raise ValueError("Size must be >= 0.")
        else:
            self.__size = value
