#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    del a_dictionary[key]
    for i, j in a_dictionary.items():
        print("{}: {}".format(i, j))
