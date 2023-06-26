#!/usr/bin/python3
def safe_print_list(listy, x):
    z = 0
    try:
        for y in range(x):
            print(listy[y], end="")
            z += 1
        print("")
    except:
        print("")
        return z
    return x
