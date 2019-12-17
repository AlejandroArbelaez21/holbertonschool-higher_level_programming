#!/usr/bin/python3
def no_c(my_string):
    for x in my_string:
        if my_string[x] == 'C' or my_string[x] == 'c':
            continue
    return (my_string)
