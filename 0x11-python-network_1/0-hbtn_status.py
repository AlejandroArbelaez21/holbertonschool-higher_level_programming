#!/usr/bin/python3
"""
import urllib
"""


import urllib.request
""" This prevent that my code not be executed when imported """
if __name__ == "__main__":
    """The funtion"""
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page))
        print("\t- utf8 content: {}".format(the_page.decode('utf8')))
