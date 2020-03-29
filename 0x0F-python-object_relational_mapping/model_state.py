#!/usr/bin/python3
"""
import the sqlalchemy and declarative_base
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
""" Main Class """


class State(Base):
    """ Class State inheritance for Base"""
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
