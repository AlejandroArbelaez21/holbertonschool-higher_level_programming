#!/usr/bin/python3
def print_list_integer(my_list=[]):
    str = "{}"
    for x in range(len(my_list)):
        print(str.format(my_list[x]))
