#!/usr/bin/python3
def weight_average(my_list=[]):
    if (my_list):
        sum = 0
        sum1 = 0
        for x, y in my_list:
            sum = sum + x * y
            sum1 = sum1 + y
        return(sum / sum1)
    return(0)
