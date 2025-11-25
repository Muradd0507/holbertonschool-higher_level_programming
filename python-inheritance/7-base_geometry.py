#!/usr/bin/python3
"""
create empty class
"""


class BaseGeometry:
    """
    empty class
    """

    def area(self):
        """
        if area is not defined, raise exception
        """
        raise Exception("area() is not implemented")

    """
    validator
    """
    def integer_validator(self, name, value):
        if (type(value) is not int):
            raise TypeError("<name> must be an integer")
        if (value <= 0):
            raise ValueError("<name> must be greater than 0")
