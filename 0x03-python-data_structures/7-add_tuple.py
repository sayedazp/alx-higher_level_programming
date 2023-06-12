#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1, len2 = len(tuple_a), len(tuple_b)
    tuple_a = 0 if len1 <= 0 else tuple_a[0], 0 if (len1) <= 1 else tuple_a[1]
    tuple_b = 0 if len2 <= 0 else tuple_b[0], 0 if (len2) <= 1 else tuple_b[1]
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
