#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in my_list:
        if i % 2 == 0:
            print(f"{i} is divisible by 2")
        else:
            print(f"{i} is not divisible by 2")
