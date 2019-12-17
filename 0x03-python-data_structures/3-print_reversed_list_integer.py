#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    str = "{}"
    my_list.reverse()
    for x in range(len(my_list)):
        print(str.format(my_list[x]))
