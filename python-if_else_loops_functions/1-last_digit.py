#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number < 0:
    number = abs(number)
    a = number % 10
else:
    a = number % 10
if a > 5:
    d = "and is greater than 5"
elif a == 0:
    d = "and is 0"
else:
    d = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, a, d), end="\n")
