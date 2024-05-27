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
        file.write(text)
        return (len(text))
#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
