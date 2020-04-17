#!/usr/bin/python3
"""
import requests
"""


import requests
from sys import argv

""" This prevent that my code not be executed when imported """
if __name__ == "__main__":
    """The funtion"""
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    dict = r.json()
    print(dict.get('id'))
