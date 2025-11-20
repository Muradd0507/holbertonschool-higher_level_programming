#!/usr/bin/python3
from functools import reduce
def uniq_add(my_list=[]):
    s = set(my_list)
    s = list(s)
    k = reduce(lambda a, b: a+b, s)
    return k
