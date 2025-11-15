#!/usr/bin/python3
result = ''
for i in range(0, 90):
    if (i == 89):
        result+="{:02} ".format(i)
    else:
        result+="{:02}, ".format(i)
print(result)
