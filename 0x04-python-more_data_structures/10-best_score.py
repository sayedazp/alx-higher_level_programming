#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = -1
    if a_dictionary is None:
        return None
    return (max(a_dictionary, key=a_dictionary.get))
