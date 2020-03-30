#!/usr/bin/python3
"""
import all mod
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format
                           (argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    other = State(name="Louisiana")
    session.add(other)
    instance = session.query(State).filter(State.name.like(other.name)).first()
    print(instance.id)
