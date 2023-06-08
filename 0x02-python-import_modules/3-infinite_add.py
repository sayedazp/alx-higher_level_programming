#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = 0
    len = len(argv) - 1
    for i in range(len):
        add += int(argv[i + 1])
    print("{}".format(add))