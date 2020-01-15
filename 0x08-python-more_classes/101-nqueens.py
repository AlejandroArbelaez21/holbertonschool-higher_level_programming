#!/usr/bin/python3
from sys import argv
if len(argv) != 2:
    print("Usage: nqueens N")
    exit (1)
elif not isinstance(argv[1], int):
    print("N must be a number")
    exit (1)
elif argv[1] < 4:
    print("N must be at least 4")    
