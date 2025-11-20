#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = set(my_list)
    s = list(s)
    k = 0
    for i in s:
        k += i
    return k
