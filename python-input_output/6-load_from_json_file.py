#!/usr/bin/python3
"""Define module"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON fil
    """
    with open(filename, "r") as file:
        return json.load(file)
