#!/usr/bin/python3
"""
import urllib
"""


import requests
if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(str(req))))
    print("\t- content: {}".format(req.text))
