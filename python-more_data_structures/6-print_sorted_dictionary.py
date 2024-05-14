#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    orderKeys = sorted(a_dictionary.keys())
    for key in orderKeys:
        print (f"{key}: {a_dictionary[key]}")
