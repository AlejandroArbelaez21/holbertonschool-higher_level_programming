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
                         passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.name FROM cities
              JOIN states ON cities.state_id = states.id WHERE states.name='{}'
              ORDER BY cities.id ASC""".format(argv[4]))

    """ loop for print the states """
    fetchall = c.fetchall()
    for cities in fetchall:
        print(cities[0], end="")
        if cities != fetchall[-1]:
            print(", ", end="")
    print()
