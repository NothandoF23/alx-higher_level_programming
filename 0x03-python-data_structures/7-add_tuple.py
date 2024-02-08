#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    size1 = len(tuple_a)
    size2 = len(tuple_b)
    added = ()
    if size1 < 2:
        tuple_a += (0, 0)
    if size2 < 3:
        tuple_b += (0, 0)
    added = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return (added)
