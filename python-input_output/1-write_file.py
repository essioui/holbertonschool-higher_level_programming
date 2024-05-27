#!/usr/bin/python3
"""Define module"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8) \
    and returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        """
        Args:
        filename: the file what we open it
        w: write mode
        encoding: we write file with coding utf-8
        """
        file.write(text)
        """Write the text"""
        return len(text)
