#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value = int(value)
    except ValueError:
        return False
    else:
        value = int(value)
        print("{:d}".format(value))
