#!/usr/bin/python3
"""introducing relationships"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()
    for x, y in session.query(City, State).\
            where(State.id == City.state_id).order_by(City.id)\
            .all():
        print("{}: ({}) {}".format(y.name, x.id, x.name))
    session.commit()
    session.close()
