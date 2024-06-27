#!/usr/bin/python3
""" State Module for HBNB project """
from panel import Column
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

    amenity_id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    place_amenities = relationship('Place', secondary=place_amenity,\
                                   back_populates='places')
