#!/usr/bin/python3
def remove_char_at(str, n):
    arr = ""
    for i in range(0, len(str)):
        if i != n:
            arr += str[i]
    return arr
