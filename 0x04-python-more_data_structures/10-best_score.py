#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = -1
    if a_dictionary is None:
        return None
    for i in list(a_dictionary):
        if a_dictionary[i] > biggest:
            biggest = a_dictionary[i]
    return biggest if biggest != -1 else None
