#!/usr/bin/python3
"""
dbjkdbvdskv
"""


class Student:
    """
    sdbsdbvdb
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__  # bütün atributlar
        else:
            result = {}
            for key in attrs:
                if key in self.__dict__:  # atribut obyektin içindədirsə
                    result[key] = self.__dict__[key]
            return result

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
