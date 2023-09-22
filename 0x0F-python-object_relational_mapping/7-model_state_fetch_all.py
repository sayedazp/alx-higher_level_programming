#!/usr/bin/python3
"""model state phase 1"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                       .format(sys.argv[1], sys.argv[2],
                               sys.argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)

session = Session()

for state in session.query(State).order_by(State.id):
    print("{}: {}".format(state.id, state.name))
