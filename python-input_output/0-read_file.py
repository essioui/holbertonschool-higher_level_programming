#!/usr/bin/python3
"""Define module"""
def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    """
    with open('filename', 'r', encoding="utf-8") as file:
        """
        Args:
        with: closed file automatically when finish and have error \
              dont using exception (__enter__ and __exit__)
        encoding: file open and read in mode utf-8

        as file: file object take contain of file for read.
        """
        print(file.read(), end="")
        """read(): mode reading"""
