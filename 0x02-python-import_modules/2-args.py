#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len = len(argv) - 1

    if (len == 0):
        print("0 arguments.")
    elif (len == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(len))
    for i in range(len):
        print("{}: {}".format(i + 1, argv[i + 1]))
