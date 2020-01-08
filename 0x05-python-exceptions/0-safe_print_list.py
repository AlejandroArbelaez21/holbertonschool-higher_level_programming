#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        cont = 0
        for y in range(x):
            print(my_list[y], end="")
            cont = cont + 1
        print()
        return (cont)
    except IndexError:
        print()
        return (cont)
