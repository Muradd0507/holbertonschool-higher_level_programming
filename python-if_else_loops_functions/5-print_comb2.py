#!/usr/bin/python3
result = ''
for i in range(0, 100):
    if (i == 99):
        result += "{:02}".format(i)
    else:
        result += "{:02}, ".format(i)
print(result)
