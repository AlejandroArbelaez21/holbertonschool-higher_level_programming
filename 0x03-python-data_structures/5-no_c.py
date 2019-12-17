#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for x in range(len(my_string)):
        if my_string[x] != 'C' and my_string[x] != 'c':
            string = string + my_string[x]
    return (string)
