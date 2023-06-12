#!/usr/bin/python3
def no_c(my_string):
    my_list = [x for x in list(my_string) if x != 'c' and x != 'C']
    print(my_string)
    return ''.join(my_list)
