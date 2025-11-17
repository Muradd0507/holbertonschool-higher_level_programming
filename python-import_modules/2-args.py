#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # skip the script name
    count = len(args)

    if count == 0:
        print("0 arguments.")
    else:
        print(f"{count} argument{'s' if count > 1 else ''}:")
        for i, arg in enumerate(args, 1):
            print(f"{i}: {arg}")
