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
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size  must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        x, y = self.__position
        if len(self.__position) != 2 or not isinstance(x, int) or not isinstance(y, int) or x <= 0 or y <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
