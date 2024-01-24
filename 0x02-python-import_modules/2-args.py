#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv) - 1
    if(size == 1):
        print("{} argument:".format(size))
        print("1: {:s}".format(argv[1]))
    elif size < 1:
        print("{} arguments.".format(size))
    else:
        print("{} arguments:".format(size))
        for i in range(size):
            print("{}: {:s}".format(i + 1 , argv[i + 1]))
