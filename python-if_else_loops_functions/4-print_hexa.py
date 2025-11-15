#!/usr/bin/python3
result = ''
for i in range(0, 99):
    if (i == 98):
        result += "{} = 0x{:x}".format(i, i)
    else:
        result += "{} = 0x{:x}\n".format(i, i)
print(result)
