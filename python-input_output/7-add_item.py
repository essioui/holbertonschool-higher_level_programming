#!/usr/bin/python3
"""Define module"""
import sys


if __name__ == '__main()__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_filen

    try:
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    """Add all arguments to the list"""
    save_to_json_file(items, "add_items.json")
    """Save the updated list back to the file"""
