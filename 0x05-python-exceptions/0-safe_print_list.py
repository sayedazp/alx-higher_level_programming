#!/usr/bin/python3
def safe_print_list(listy=[], x=0):
    z = 0
    try:
        for y in range(x):
            print("{}".format(listy[y]), end="")
            z += 1
        print("")
    except IndexError:
        print("")
        return z
    return x
