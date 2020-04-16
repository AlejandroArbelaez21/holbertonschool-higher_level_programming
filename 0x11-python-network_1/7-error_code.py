#!/usr/bin/python3
"""
import requests
"""


import requests
from sys import argv

""" This prevent that my code not be executed when imported """
if __name__ == "__main__":
    """The funtion"""
    try:
        r = requests.get(argv[1])
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError:
        print("Error code: {}".format(r.status_code))
