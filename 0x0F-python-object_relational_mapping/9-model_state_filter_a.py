#!/usr/bin/python3
""" Prints the first State obj from database """


from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        state = session.query(State).filter(State.name.contains('a'))

        try:
            for row in state:
                print(f"{row.id}: {row.name}")
        except Exception:
            print()
