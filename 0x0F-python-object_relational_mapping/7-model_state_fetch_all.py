#!/usr/bin/python3
""" sessionmaker"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    #create the sqlalchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    #create a session factor
    Session = sessionmaker(bind=engine)

    #create the session object
    session = Session()

    #retrive all states
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
