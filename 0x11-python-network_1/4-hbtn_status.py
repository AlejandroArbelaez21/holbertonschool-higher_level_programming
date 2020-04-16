#!/usr/bin/python3
"""
import urllib
"""


import requests
""" This prevent that my code not be executed when imported """
if __name__ == "__main__":
    """The funtion"""
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(str(req))))
    print("\t- content: {}".format(req.text))
