#!/usr/bin/python3
"""Define a Class."""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class
        Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) is a_class and a_class != object:
        return True
    if type(obj) is object:
        return False
    return False
