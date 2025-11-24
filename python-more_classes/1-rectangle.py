#!/usr/bin/python3
"""
More Classes
"""


class Rectangle:
    """
    This class defines a rectangle
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        if (type(self.__width) is not int):
            raise TypeError("width must be an integer")
        if (type(self.__height) is not int):
            raise TypeError("height must be an integer")
        if (self.__width <= 0):
            raise ValueError("width must be >= 0")
        if (self.__height <= 0):
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be >= 0")
        self.__height = value
