#!/usr/bin/python3
char = ""
for alphabet in range(97, 123):
    char += "{:c}".format(alphabet) # you can use .format(alph),end=""
print(char)
print(len(char))