#!/usr/bin/python3

def no_c(my_string):
    new = list(my_string)
    new_list = ''
    for char in new:
        if char != 'c' and char != 'C':
            new_list += char
    return new_list
if __name__ == '__main__':
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
