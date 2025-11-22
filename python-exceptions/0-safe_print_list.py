#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    k = 0
    try:
        for i in my_list:
            if (k < x):
                print("{:d}".format(i), end='')
            k += 1
        print()
        return k

    except IndexError:
        return None
