#!/usr/bin/python3
"""
Define addition integer function
"""


def add_integer(a, b=98):
    """
    Return the sum of a and b
    declaration a and b before use function
    Raise: type error
    if type a or b is not integer and not float
    return int a + int b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/0-add_integer.txt")
