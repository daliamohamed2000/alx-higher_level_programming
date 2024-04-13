#!/usr/bin/python3

""" model state """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class of attribute of a state.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
