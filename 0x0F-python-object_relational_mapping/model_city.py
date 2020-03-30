#!/usr/bin/python3
"""
import the sqlalchemy and declarative_base
"""


from model_state import Base
from sqlalchemy import Column, Integer, String


class City(Base):
    """ Class City inheritance for Base"""
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, primary_key=True, ForeignKey("states.id"))
