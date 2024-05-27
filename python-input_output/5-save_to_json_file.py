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
    with open(filename, 'w') as json_file:
        json.dump(my_obj, json_file)
