#!/usr/bin/python3
def search_replace(my_list, search, replace):
    myList = []
    for i in my_list:
        if i == search:
            myList.append(replace)
        else:
            myList.append(i)
    return (myList)
