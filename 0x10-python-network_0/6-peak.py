#!/usr/bin/python3
"""peak function module"""


def find_peak(list_of_integers):
    """find peak function using log(n) algorithm
    """
    start = 0
    end = len(list_of_integers) - 1
    for i in range(len(list_of_integers)):
        mid = int((end + start)/2)
        if ((mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1])
            and (mid == len(list_of_integers) - 1 or
                 list_of_integers[mid] >= list_of_integers[mid + 1])):
            return list_of_integers[mid]
        elif (mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]):
            end = mid - 1
        else:
            start = mid + 1
    return None
