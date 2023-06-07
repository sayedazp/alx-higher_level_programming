#!/usr/bin/python3
for i in range(0, 10):
    for z in range(i+1, 10):
        if (i != 8 or z != 9):
            print("{}{}".format(i, z), end=', ')
        else:
            print("{}{}".format(i, z))
