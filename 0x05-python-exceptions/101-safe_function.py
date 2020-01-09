#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return (fct(args[0], args[1]))
    except ZeroDivisionError as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return (None)
    except IndexError as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return (None)
