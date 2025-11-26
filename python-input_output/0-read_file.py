#!/usr/bin/python3
"""
read it
"""

def read_file(filename=""):
    """
    read it
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()
