#!/usr/bin/python3
""" Prints the first State obj from database """


import MySQLdb
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).first()
        print(f"{state.id}: {state.name}")
    except Exception:
        print(Nothing)
