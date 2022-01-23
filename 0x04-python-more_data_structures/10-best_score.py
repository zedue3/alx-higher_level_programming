#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        value = None
        key = None
        for k in a_dictionary.keys():
            if value is None or a_dictionary[k] > value:
                value = a_dictionary[k]
                key = k
        return key
