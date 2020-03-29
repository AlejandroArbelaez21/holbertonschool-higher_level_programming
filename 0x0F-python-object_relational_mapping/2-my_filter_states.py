#!/usr/bin/python3
"""
import the module MySQLdb and argv from sys
"""


import MySQLdb
from sys import argv

""" This prevents that my code should not be executed when imported """
if __name__ == "__main__":
    """ Here realice a query and make a cursor """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], argument = argv[4])
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name='{}'
              ORDER BY id""".format(argument))

    """ loop for print the states """
    for state in c.fetchall():
        if state[1] == argument:
            print(state)
