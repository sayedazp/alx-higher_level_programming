#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    sum = 0
    conv_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                                          'D': 500, 'M': 1000}
    for i, v in enumerate(roman_string):
        if i < len(roman_string) - 1:
            if (conv_dict[roman_string[i]] < conv_dict[roman_string[i + 1]]):
                sum += -1*conv_dict[v]
            else:
                sum += conv_dict[v]
        else:
            sum += conv_dict[v]
    return sum
