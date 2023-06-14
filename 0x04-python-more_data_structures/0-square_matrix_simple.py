#!/usr/bin/python3
# def square_matrix_simple(matrix=[]):
#     listy = [[s**2 for s in x] for x in matrix ]
#     return listy

def square_matrix_simple(matrix=[]):
    listy = []
    for row in matrix:
        new = list(map(lambda x: x**2, row))
        listy.append(new)
    return listy
