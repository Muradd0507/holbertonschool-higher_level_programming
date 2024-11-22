#!/usr/bin/python3
"""
learning classes
"""


class Square:
    """
    raising errors
    """

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        self__size=value
        return self.__size

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

