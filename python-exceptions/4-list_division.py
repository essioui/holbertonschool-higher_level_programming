#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    i = 0
    try:
        while i < list_length:
            try:
                num1 = my_list_1[i]
            except IndexError:
                num1 = None
                
            try:
                num2 = my_list_2[i]
            except IndexError:
                num2 = None
                
            if num1 is None or num2 is None:
                print("out of range")
                result.append(0)
            elif not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                print("wrong type")
                result.append(0)
            elif num2 == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(num1 / num2)
                
            i += 1
            
    finally:
        return result
