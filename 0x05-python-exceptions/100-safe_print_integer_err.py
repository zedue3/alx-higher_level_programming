#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        return value
    except:
        print("Exception: Unknown format code \'d\' for object of type \'str\'")
        return False
if __name__ == "__main__":
    safe_print_integer_err = \
    __import__('100-safe_print_integer_err').safe_print_integer_err

    value = 89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
