#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    new_tuple = ()
    if size == 0:
        new_tuple = 0, None
        return (new_tuple)
    else:
        new_tuple = size, sentence[0]
        return (new_tuple)
