#!/usr/bin/python3
from json import dump


def save_to_json_file(my_obj, filename):
    with open(filename, mode="w", encoding="UTF-8") as file:
        return (dump(my_obj, file))
