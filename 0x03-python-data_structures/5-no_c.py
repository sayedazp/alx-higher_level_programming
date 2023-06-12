#!/usr/bin/python3
def no_c(my_string):
    idx = 0
    my_list = list(my_string)
    for i in my_list:
        if my_list[idx] == 'c':
            del my_list[idx]
        idx += 1
    return ''.join(my_list)
