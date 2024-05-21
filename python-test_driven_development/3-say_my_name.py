#!/usr/bin/python3
"""
Module print my first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Print my name
    Args: frist_name: must be a string
          frist_name: must be a string
    Return:
    My name is first_name last_name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if last_name and not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name} ")

