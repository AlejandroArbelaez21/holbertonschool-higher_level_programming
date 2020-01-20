#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        cont = 0
        for y in range(len(self)):
            if type(self[cont]) is not int:
                raise TypeError("unorderable types: int() < str()")
                cont += 1
        my_list = self[:]
        my_list.sort()
        print(my_list)
