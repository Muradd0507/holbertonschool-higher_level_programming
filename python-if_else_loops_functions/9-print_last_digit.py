#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
        a = number % 10
    else:
        a = number % 10
    print(a, end='')
    return a
