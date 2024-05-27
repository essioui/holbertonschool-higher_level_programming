#!/usr/bin/python3
"""Define module"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save the oblect to json file
    Args:
    my_obj: the object to be savee
    filename: the name of the json file
    """

    try:
        with open(filename, 'w') as json_file:
            json.dump(my_obj, json_file)
    except TypeError as e:
        raise TypeError(f"Object {my_obj} cannot be serialized to JSON") from e
    except PermissionError as e:
        raise PermissionError(f"No permission to write to file {filename}") from e
