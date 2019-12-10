#!/usr/bin/python3
def uppercase(str):
    for x in str[:]:
        y = ord(x)
        if y > 96 and y < 123:
            y = y - 32
        print("{}".format(chr(y)), end="")
    print()
