#!/usr/bin/python3
"""
Define class MyList
"""


class MyList:
    """
    MyList inherits from list
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
