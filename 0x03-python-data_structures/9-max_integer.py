#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        size = len(my_list)
        i = 1
        maxx = my_list[0]
        while i < size:
            if maxx < my_list[i]:
                maxx = my_list[i]
            i += 1
        return (maxx)
    else:
        return (None)
