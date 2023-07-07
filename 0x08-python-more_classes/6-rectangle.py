#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.
        Attributes:
            number_of_instances (int): num of recs
    """
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """initialize a new rectangle
            Args:
                width (int): rec width
                height (int): rec height
        """
        type(self).number_of_instances += 1
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

    def __str__(self):
        """text representations for user"""
        if self.width == 0 or self.height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """formal obj repr"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """destructor"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
