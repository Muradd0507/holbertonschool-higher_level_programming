#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        if (my_list[i] == idx):
            return my_list[i + 1]
        else:
            return None
