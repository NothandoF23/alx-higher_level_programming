#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv)
    summ = 0
    for i in range(1, size):
        summ += int(argv[i])
    print("{}".format(summ))
