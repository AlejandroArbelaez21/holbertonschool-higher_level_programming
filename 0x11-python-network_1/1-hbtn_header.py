#!/usr/bin/python3
"""
import urllib
"""


import urllib.request
from sys import argv

""" This prevent that my code not be executed when imported """
if __name__ == "__main__":
    """The funtion"""
    req = argv[1]
    with urllib.request.urlopen(req) as response:
        the_page = response.info()
        print(the_page.get('X-Request-Id'))