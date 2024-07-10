#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.config import ENV_VAR
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    # places = relationship('Place', back_populates='user',\
    #                     cascade="all, delete-orphan")
    # reviews = relationship('Review', back_populates='user',
    #                     cascade="all, delete-orphan")
