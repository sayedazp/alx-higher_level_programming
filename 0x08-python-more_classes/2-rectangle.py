#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """initialize a new rectangle
            Args:
                width (int): rec width
                height (int): rec height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width"""
        return (self.__width)

    @property
    def height(self):
        """get height"""
        return (self.__height)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))

    def area(self):
        """calc area"""
        return (self.width * self.height)
