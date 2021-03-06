#!/usr/bin/python3
"""
import the module json
"""


from json import dumps, loads


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
        my_list = []
        if list_objs is None:
            with open(cls.__name__ + ".json", "w", encoding="UTF-8") as file:
                return file.write(cls.to_json_string(my_list))
        else:
            for ob in list_objs:
                my_dict = ob.to_dictionary()
                my_list.append(my_dict)
            with open(cls.__name__ + ".json", "w", encoding="UTF-8") as file:
                return file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        my_list = []
        if json_string is None or json_string == []:
            return my_list
        else:
            my_list = loads(json_string)
            return my_list

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        file = cls.__name__ + ".json"
        list = []
        try:
            with open(file, mode="r") as f:
                list = cls.from_json_string(f.read())
                return [cls.create(**my_dict) for my_dict in list]
        except:
            pass
        return list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        my_list = []
        if list_objs is None:
            with open(cls.__name__ + ".csv", "w", encoding="UTF-8") as file:
                return file.write(cls.to_json_string(my_list))
        else:
            for ob in list_objs:
                my_dict = ob.to_dictionary()
                my_list.append(my_dict)
            with open(cls.__name__ + ".csv", "w", encoding="UTF-8") as file:
                return file.write(cls.to_json_string(my_list))

    @classmethod
    def load_from_file_csv(cls):
        file = cls.__name__ + ".csv"
        list = []
        try:
            with open(file, mode="r") as f:
                list = cls.from_json_string(f.read())
                return [cls.create(**my_dict) for my_dict in list]
        except:
            pass
        return list
