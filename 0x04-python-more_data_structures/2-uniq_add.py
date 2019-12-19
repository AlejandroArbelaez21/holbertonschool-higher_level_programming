#!/usr/bin/python3
def uniq_add(my_list=[]):
    y = 0
    for x in set(my_list):
        y += x
    return (y)
