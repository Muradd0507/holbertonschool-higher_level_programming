#!/usr/bin/python3
def print_list_integer(my_list=[]):
    s=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in my_list:
        for j in s:
            print("{:d}".format(i))
