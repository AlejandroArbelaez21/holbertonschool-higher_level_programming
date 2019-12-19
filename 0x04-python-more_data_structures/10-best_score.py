#!/usr/bin/python3
def best_score(a_dictionary):
    y = 0
    str = ""
    if (a_dictionary):
        for x in a_dictionary:
            if (a_dictionary[x] > y):
                y = a_dictionary[x]
                str = x
        return(str)
    else:
        return (None)
