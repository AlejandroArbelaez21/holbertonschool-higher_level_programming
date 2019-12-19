#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for x in a_dictionary:
        if (key in a_dictionary):
            a_dictionary[key] = value
        else:
            d1 = {key: value}
            a_dictionary.update(d1)
        return(a_dictionary)
