#!/usr/bin/python3
alphabet =""
for i in range(122, 64, -1):
    if i % 2 == 0:
        alphabet += chr(i)
    else :
        alphabet += chr(i).upper()
print(alphabet, end="")

