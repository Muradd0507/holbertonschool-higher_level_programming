#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    a = number % 10
    if number < 0:
        a = -a
    print(a)
    return a
