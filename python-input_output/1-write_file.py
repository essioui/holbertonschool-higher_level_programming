#!/usr/bin/python3
def write_file(filename="", text=""):
    """Define module"""
    with open(filename, 'w', encoding='utf-8') as file:
        """
        filename: the file what we open it
        w: write mode
        encoding: we write file with coding utf-8
        """
        file.write(text)
        return (len(text))
