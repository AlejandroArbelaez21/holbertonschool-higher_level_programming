#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif argv[2] == '+':
        a = argv[1]
        b = argv[3]
        print("{:d} + {:d} = {:d}".format(int(a), int(b), add(int(a), int(b))))
        exit(0)
    elif argv[2] == '-':
        a = argv[1]
        b = argv[3]
        print("{:d} - {:d} = {:d}".format(int(a), int(b), sub(int(a), int(b))))
        exit(0)
    elif argv[2] == '*':
        a = argv[1]
        b = argv[3]
        print("{:d} * {:d} = {:d}".format(int(a), int(b), mul(int(a), int(b))))
        exit(0)
    elif argv[2] == '/':
        a = argv[1]
        b = argv[3]
        print("{:d} / {:d} = {:d}".format(int(a), int(b), div(int(a), int(b))))
        exit(0)
