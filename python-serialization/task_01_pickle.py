#!/usr/bin/python3
"""Define module"""
import pickle


class CustomObject:
    """
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize object and save it
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    
    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize object and load it
        """
        with open(filename, 'rb') as file:
            return (pickle.load(file))
