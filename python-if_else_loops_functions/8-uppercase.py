#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            # ord(i) transfer letter to number
            # and ord('a') = 97 & ord('z') = 123
            i = chr(ord(i) - 32)
            # chr() function transfer number to letter & -32 for uppercase
        print("{}".format(i), end="")
    print("")
