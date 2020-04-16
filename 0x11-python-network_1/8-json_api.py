#!/usr/bin/python3
"""
import requests
"""


import requests
from sys import argv

""" This prevent that my code not be executed when imported """
if __name__ == "__main__":
    """The funtion"""
    a = argv[1][0]
    if len(argv) == 1:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': ''})
        print("No result")
    elif argv[1].isdigit():
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': ''})
        print("No result")
    else:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': a})
        if r.text[0] != '{' and r.text[-1] != '}':
            print("Not a valid JSON")
        else:
            id = r.text[6:10]
            letter = r.text[19:-3]
            print("[{}] {}".format(id, letter))
