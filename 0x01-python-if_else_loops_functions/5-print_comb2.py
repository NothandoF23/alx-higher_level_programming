#!/usr/bin/python3
for ch in range(0, 100):
    if ch < 10:
        print("0{}".format(ch), end=", ")
    else:
        print("{}".format(ch), end=", ")

