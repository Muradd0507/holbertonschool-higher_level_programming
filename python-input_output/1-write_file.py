#!/usr/bin/python3
"""
writee
"""


def write_file(filename="", text=""):
    """
    writee
    """
    with open(filename, 'w', encoding='utf-8') as f:
        print(f.write(text))
