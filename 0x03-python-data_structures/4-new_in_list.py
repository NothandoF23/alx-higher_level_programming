#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list) - 1
    new_list = my_list[:]
    if idx < 0 or idx > size:
        return (new_list)
    else:
        new_list[idx] = element
        return (new_list)
