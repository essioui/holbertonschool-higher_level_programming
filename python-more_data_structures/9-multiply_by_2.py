#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiply_num = {}
    for key, value in a_dictionary.items():
        multiply_num[key] = value *2
    return (multiply_num)
