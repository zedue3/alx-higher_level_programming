#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if x < len(my_list):
            return my_list(x)
        else:
            return my_list
    except:
        return my_list
