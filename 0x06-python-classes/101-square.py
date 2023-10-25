#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """ This class represents a square with a given size and position.
    """

    def __str__(self):
        """Defines the string representation of a Square."""
        if self.size == 0:
            return ""
        else:
            return "\n" * self.position[1] + "\n".join(" " * self.position[0] + "#" * self.size for _ in range(self.size))

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets or sets the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the Square."""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        if value < 0:
            raise ValueError("Size must be >= 0.")
        self.__size = value

    @property
    def position(self):
        """Gets or sets the position of the Square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the Square."""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("Position must be a tuple of 2 non-negative integers.")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the Square."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints a square of '#'symbols according to size, position values."""
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            print("\n".join(" " * self.position[0] + "#" * self.size for _ in range(self.size)))
