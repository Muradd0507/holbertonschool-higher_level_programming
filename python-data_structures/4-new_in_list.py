#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    s = []
    for i in range(len(my_list)):
        if (idx < 0 or idx > len(my_list)):
            return my_list
        if (i == idx):
            s.append(element)
        else:
            s.append(my_list[i])
    return s
