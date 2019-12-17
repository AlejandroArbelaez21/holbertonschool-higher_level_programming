#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = []
    for x in range(len(my_list)):
        if ((my_list[x] % 2) == 0):
            list.append(True)
        else:
            list.append(False)
    return(list)
