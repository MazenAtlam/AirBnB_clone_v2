#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = Column(String(128), nullable=False)
    # cities = relationship('City', back_populates="state")
