#!/usr/bin/python3
""" All states via SQLAlchemy """


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
    table = session.query(State).all()

    try:
        for state in table:
            print(f"{state.id}: {state.name}")
    except Exception:
        print()
