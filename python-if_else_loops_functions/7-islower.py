#!/usr/bin/env python3
def islower(letter):
    if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
        return True
    else:
        return False
print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))

