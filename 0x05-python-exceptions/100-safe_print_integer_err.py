#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError as ne:
        print("Exception:", ne)
        return (False)
    except TypeError as ne:
        print("Exception:", ne)
        return (False)
