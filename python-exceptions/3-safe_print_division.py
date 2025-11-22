#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except(ZeroDivisionError, TypeError):
        result = None
    finally:
        lresult = "Inside result: {}".format(result)
        return lresult
