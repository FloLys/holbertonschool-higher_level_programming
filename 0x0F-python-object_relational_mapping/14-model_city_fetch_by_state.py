#!/usr/bin/python3
""" All states via SQLAlchemy """


import MySQLdb
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        cities = (session.query(City, State).join(State, State.id ==
                                                  City.state_id).all())

        for city, state in cities:
            print(f"{state.name}: ({city.id}) {city.name}")
