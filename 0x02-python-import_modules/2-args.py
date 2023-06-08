#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len = len(argv)

    if (len == 0):
        print("0 arguments.")
    elif (len == 1):
        print("1 argument:")
        for idx, x in enumerate(argv):
            print("{}: {}".format(idx + 1, x))
    else:
        print("{} arguments:".format(len))
        for idx, x in enumerate(argv):
            print("{}: {}".format(idx + 1, x))
