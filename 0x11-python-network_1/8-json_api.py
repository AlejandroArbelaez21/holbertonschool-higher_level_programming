#!/usr/bin/python3
"""
import requests
"""


import requests
from sys import argv

""" This prevent that my code not be executed when imported """
if __name__ == "__main__":
    """The funtion"""
    letter = ""
    try:
        letter = argv[1]
    except:
        pass
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        file = r.json()
        if file == {}:
            print("No result")
        else:
            print("[{}] {}".format(file.get('id'), file.get('name')))
    except:
        print("Not a valid JSON")
