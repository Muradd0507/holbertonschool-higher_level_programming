#!/usr/bin/python3
def islower(c):
    letter = ord(c)
    if letter in range(97, 122):
        return True
    elif letter in range(65, 90):
        return False
