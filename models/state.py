#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer


class State(BaseModel):
    """ State class """
    
    states_id = Column(Integer, primary_key=True)
    name = ""
