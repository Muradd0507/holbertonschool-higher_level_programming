#!/usr/bin/python3
import random

number = random.randint(-10, 10)
if number > 0:
    print("is positive", end="\n")
elif number == 0:
    print("is zero", end="\n")
else:
    print("is negative", end="\n")