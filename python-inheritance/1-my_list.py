#!/usr/bin/python3
"""Create a MyList Class."""


class MyList(list):
    """class inherits of list."""
    def print_sorted(self):
        """Sorts a list."""
        print(sorted(self))
