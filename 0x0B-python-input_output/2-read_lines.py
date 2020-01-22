#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, mode="r", encoding="UTF-8") as file:
        if nb_lines <= 0 or nb_lines >= len(file.readlines()):
            print(file.read(), end="")
        else:
            len_lines = file.readlines()
            for line in range(nb_lines):
                print(len_lines, end="")
