#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = (number % -10)
    if lastdigit == 0:
        print("Last digit of {0} is {1} and is 0".format(number,lastdigit))
    else:
        print("Last digit of {0} is {1} and is less than 6 and not 0".format(number,lastdigit))
else:
    lastdigit = (number % 10)
    if lastdigit == 0:
        print("Last digit of {0} is {1} and is 0".format(number,lastdigit))
    elif lastdigit < 6:
        print("Last digit of {0} is {1} and is less than 6 and not 0".format(number,lastdigit))
    else:
        print("Last digit of {0} is {1} and is greater than 5".format(number,lastdigit))
