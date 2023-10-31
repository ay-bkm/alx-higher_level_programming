#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """Defines a rectangle class."""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle class."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """extracts the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """extracts the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
