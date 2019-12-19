#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = my_list.copy()
    for x in range(len(list)):
        if (list[x] == search):
            list[x] = replace
    return (list)
