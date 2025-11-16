#!/usr/bin/python3
def uppercase(str):
    result = ''
    k = ''
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            k = chr(ord(str[i]) - 32)
            result += k
        else:
            result += str[i]
    print("{}".format(result))
