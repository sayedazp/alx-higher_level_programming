#!/usr/bin/python3
def weight_average(my_list=[]):
    my_len = len(my_list)
    if my_len == 0:
        return 0
    new_list = [x[0]*x[1] for x in my_list]
    sum = 0
    sum2 = 0
    for i, v in enumerate(new_list):
        sum += v
        sum2 += my_list[i][1]
    return sum/sum2
