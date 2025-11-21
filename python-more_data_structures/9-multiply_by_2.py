#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    k = {}
    for i, v in a_dictionary.items():
        v = v * 2
        k[i] = v
    return k
