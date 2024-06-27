#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer


class State(BaseModel):
    """ State class """
    name = ""
