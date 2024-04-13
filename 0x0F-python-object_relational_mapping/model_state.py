""" model state """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class state(Base):

    """
    Class of attribute of a state.
    """

    __tablename__ = 'states'
    id = Column(Integer, Unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
