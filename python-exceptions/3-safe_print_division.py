#!/usr/bin/python3
def safe_print_division(a, b):
    c = None
    if isinstance(a, int) and isinstance(b, int):
        try:
            c = a / b
            print("Inside result: {}".format(c), end="\n")
            return ("{}".format(c))
        except ZeroDivisionError:
            print("Inside result: {}".format(c), end="\n")
            return (None)
        finally:
            return ("{}".format(c))
