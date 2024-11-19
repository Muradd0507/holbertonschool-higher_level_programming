#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if ord(i) in range(97, 123):
            result += "{}".format(chr(ord(i) - 32))
        else:
            result += "{}".format(i)

    print(result, end="")
