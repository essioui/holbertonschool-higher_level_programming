#!/usr/bin/python3
"""Define module"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end \
    of a text file (UTF8) and returns the number of characters added.
    Args:
    filename: file in string we open it
    text: that text in file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        """
        Args:
        'a': append mode
        """
        file.write()
        return (len(text))
