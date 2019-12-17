#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        a = 0
        for x in range(len(my_list)):
            if a < my_list[x]:
                a = my_list[x]
        return (a)
    return(None)
