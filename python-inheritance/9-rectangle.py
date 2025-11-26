#!/usr/bin/python3
"""
Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """

    def __init__(self, width, height):
        """Self"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        self.area()

    def __str__(self):
        print("[Rectangle] {}/{}".format(self.__width, self.__height))
        return self.__width * self.__height
