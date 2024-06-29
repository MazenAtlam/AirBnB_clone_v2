#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.config import ENV_VAR
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if ENV_VAR['hbnb_storage_type'] == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)

        # places = relationship('Place', back_populates='cities',\
        #                         cascade="all, delete-orphan")    
    else:
            state_id = ""
            name = ""
