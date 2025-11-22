#!/usr/bin/python3
def safe_print_integer(value):
    try:
        test = value + 1
    except (ValueError, TypeError):
        return False
    else:
        print("{:d}".format(value))
        return True
