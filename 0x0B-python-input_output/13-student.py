#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            my_dict = {}
            for y in attrs:
                if y in self.__dict__:
                    my_dict[y] = self.__dict__[y]
            return (my_dict)

    def reload_from_json(self, json):
        if type(json) is dict:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
        else:
            pass
