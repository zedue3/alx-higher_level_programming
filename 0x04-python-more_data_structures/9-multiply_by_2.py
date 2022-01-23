#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new_dictionary = dict(a_dictionary)
        for key, value in new_dictionary.items():
            new_dictionary[key] = value * 2
        return (new_dictionary)

if __name__ == "__main__":
    print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary
    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
