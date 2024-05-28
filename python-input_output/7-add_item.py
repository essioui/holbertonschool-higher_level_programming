#!/usr/bin/python3
"""Define module"""
import sys
from os.path import exists


if __name__ == '__main()__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_filen

    filename = "add_item.json"


    if exists(filename):
        """Load list from the file if it exists, otherwise create a new list"""
        items = load_from_json_file(filename)
    else:
        items = []

    items.extend(sys.argv[1:])
    """Add all arguments to the list"""

    save_to_json_file(items, filename)
    """save arguments in the file"""
