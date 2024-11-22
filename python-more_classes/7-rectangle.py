#!/usr/bin/python3
"""
efjwl
"""


class Rectangle:
    """
    hfewfhwer
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.width > 0 and self.height > 0:
            return 2 * (self.__width + self.__height)
        else:
            return 0

    def __str__(self):
        if self.width > 0 and self.height > 0:
            return "\n".join(
                [
                    str(self.print_symbol) * self.width
                    for _ in range(self.height)
                ]
            )

        else:
            return ''

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
