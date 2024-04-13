#!/usr/bin/python3

""" model state """
from model_state import BASE
from sqlalchemy import Column, Integer, String, Foreignkey
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class city(Base):
    """
    City Base class
    """

    __tablename__ = 'cities'
    id = Column(Integer, Unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, Foreignkey("states_id"), nullable=False)
