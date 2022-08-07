#!/usr/bin/python3
""" Print the obj with the name passed as arg4 """


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
        state = session.query(State).filter(State.name == argv[4])\
                .one_or_none()

        try:
            print(f"{state.id}")
        except Exception:
            print("Not found")
