#!usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for i in my_list:
            if counter < x:
                print("{}".format(my_list[counter]), end="")
                counter += 1
        print()
    except TypeError:
        pass
    finally:
        return (counter)
