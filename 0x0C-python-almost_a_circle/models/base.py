#!/usr/bin/python3
from json import dumps
"""
import the module json
"""


class Base:
    """
    The class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ define the __init__"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ define the staticmethod"""
        if list_dictionaries is None:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ define the classmethod"""
        if list_objs is None:
            str_json = "[]"
        else:
            return cls.to_json_string(list_objs)
