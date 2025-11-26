#!/usr/bin/python3
"""Square"""


class Square(Rectangle):
    """sqclass"""

    def __init__(self, size):
        """initialization"""
        size.integer_validator()
        self.__size = size

    def area(self):
        """areaa"""
        return self.__size * self.__size
