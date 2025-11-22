#!/usr/bin/python3
def safe_print_integer(value):
    try:
        test = value + 1
        value_int = int(value)
        if (value != value_int):
            return False
    except (ValueError, TypeError):
        return False
    else:
        print("{:d}".format(value))
        return True
