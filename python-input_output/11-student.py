#!/usr/bin/python3
"""Create student class"""


class Student:
    """Class present a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        if attrs is None:
            return self.__dict__
        if type(attrs) is list:
            for elements in attrs:
                if type(elements) is str:
                    dict = self.__dict__
                    if elements in dict:
                        new_dict[elements] = dict[elements]
                else:
                    return self.__dict__
            return new_dict

    def reload_from_json(self, json):
        """
        Args:
        json (json): is file of type json
        """
        for key, value in json.items():
            self.__dict__[key] = value
