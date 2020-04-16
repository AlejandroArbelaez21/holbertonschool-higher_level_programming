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
    email = {'email': argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode()
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf8'))
