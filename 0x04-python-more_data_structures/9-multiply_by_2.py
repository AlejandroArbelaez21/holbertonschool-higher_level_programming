#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = {}
    for x, y in a_dictionary.items():
        my_dict[x] = y * 2
    return (my_dict)
