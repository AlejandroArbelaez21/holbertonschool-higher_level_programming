#!/usr/bin/python3
"""
import all mod
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """ This prevents that my code should not be executed when imported """
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format
                           (argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query.first(State).order_by(State.id):
        if instance is None:
            print("Nothing")
        else:
            print("{}: {}".format(instance.id, instance.name))
