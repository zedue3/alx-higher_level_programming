#!/usr/bin/python3
if __name__ == "__main__":
    from calulator_1 import add, sub, mul, div
    a = 5
    b = 10
    print("{:d} + {:d} = {:d}".format(a,b, add(a,b)))
    print("{:d} - {:d} = {:d}".format(a,b, sub(a,b)))
    print("{:d} * {:d} = {:d}".format(a,b, mul(a,b)))
    print("{:d} / {:d} = {:d}".format(a,b, div(a,b)))
