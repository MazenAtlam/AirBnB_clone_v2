#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.config import ENV_VAR
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if ENV_VAR['hbnb_storage_type'] == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates="state")
    else:
        name = ""

