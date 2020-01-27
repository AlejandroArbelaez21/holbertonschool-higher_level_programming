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
        """ define the __init__
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    """
    Static method for json string
    """
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return dumps(list_dictionaries)
