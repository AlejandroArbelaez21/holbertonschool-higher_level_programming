#!/usr/bin/python3
"""
import urllib
"""


import urllib.request
import urllib.parse
from sys import argv

""" This prevent that my code not be executed when imported """
if __name__ == "__main__":
    """The funtion"""
    url = argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode('utf8'))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
