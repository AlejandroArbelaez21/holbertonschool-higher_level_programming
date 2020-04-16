#!/usr/bin/python3
"""
import requests
"""


import requests
from sys import argv

""" This prevent that my code not be executed when imported """
if __name__ == "__main__":
    """The funtion"""
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
