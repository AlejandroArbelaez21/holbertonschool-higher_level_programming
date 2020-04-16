#!/usr/bin/python3
"""
import urllib
"""


import requests
from sys import argv

""" This prevent that my code not be executed when imported """
if __name__ == "__main__":
    """The funtion"""
    req = argv[1]
    the_page = requests.get(req)
    dict = the_page.headers
    print(dict.get('X-Request-Id'))
