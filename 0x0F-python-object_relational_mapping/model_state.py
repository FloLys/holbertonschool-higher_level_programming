#!/usr/bin/python3
""" First state model """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Class State takes from tablename states
        with it its columns id and name
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
