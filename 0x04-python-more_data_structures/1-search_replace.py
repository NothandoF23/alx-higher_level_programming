#!/usr/bin/python3
def search_replace(my_list, search, replace):
    size = len(my_list)
    new = my_list.copy()
    for i in range(0, size):
        if my_list[i] == search:
            new[i] = replace
    return (new)
