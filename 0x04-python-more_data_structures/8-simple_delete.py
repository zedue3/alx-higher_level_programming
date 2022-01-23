#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        new_dictionary = del a_dictionary[key]
    return (new_dictionary)
