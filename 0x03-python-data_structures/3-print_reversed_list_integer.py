#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        my_list.reverse()
        for i in range(len(my_list)):
            print('{:d}'.format(my_list[i]))


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
