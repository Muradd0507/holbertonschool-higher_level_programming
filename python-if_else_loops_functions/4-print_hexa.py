#!/usr/bin/python3
result=''
    if (i == 98):
        result += "{} = 0x{:x}".format(i, i)
    else:
        result += "{} = 0x{:x}\n".format(i, i)
print(result)
