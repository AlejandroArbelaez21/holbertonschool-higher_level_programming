#!/usr/bin/python3
"""
import all mod
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format
                           (argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance, city in session.query(State, City)\
                                 .filter(State.id == City.state_id)\
                                 .order_by(City.id):
        print("{}: ({}) {}".format(instance.name, city.id, city.name))
