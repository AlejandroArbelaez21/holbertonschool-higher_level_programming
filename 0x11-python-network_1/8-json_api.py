#!/usr/bin/python3
"""
import requests
"""


import requests
from sys import argv

""" This prevent that my code not be executed when imported """
if __name__ == "__main__":
    """The funtion"""
    if len(argv) == 1:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': ''})
        print("No result")
    elif argv[1].isdigit():
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': ''})
        print("No result")
    else:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': argv[1]})
        id = r.text[6:10]
        letter = r.text[19:-3]
        print("[{}] {}".format(id, letter))
