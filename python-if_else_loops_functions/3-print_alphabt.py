#!/usr/bin/python3
asc = ''
for i in range(97, 123):
    if (i != 101 and i != 113):
        asc += chr(i).lower()
print("{}".format(asc), end='')
