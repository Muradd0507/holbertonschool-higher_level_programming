#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    s = []
    for i in range(len(my_list)):
        if (idx == i):
            pass
        else:
            s.append(my_list[i])
    return s
