#!/usr/bin/python3
if __name__ == "__main__":
    from hidden import *
    functions = dir()
    size = len(functions)
    for i in range(size):
        if functions[i][:2] != "_":
            print("{:s}".format(functions[i]))
