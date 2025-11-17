#!/usr/bin/python3
import sys
if (__name__ == "__main__"):
    result = 0
    args = sys.argv[1:]
    for i in args:
        result += int(i)
    print("{}".format(result))
