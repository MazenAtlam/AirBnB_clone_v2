#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """ This class defines an amenity by various attributes
    """
    __tablename__ = 'amenities'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = Column(String(128), nullable=False)

    # place_amenities = relationship('Place', secondary=place_amenity,\
                                # back_populates='places')
