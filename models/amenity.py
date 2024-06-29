#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.config import ENV_VAR
from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship


# from .place import Place

# metadata = Base.metadata
# place_amenity = Table('place_amenity', metadata,\
#                     Column('place_id', String(60), ForeignKey('places.id'),\
#                         primary_key=True, nullable=False),\
#                     Column('amenity_id', String(60), ForeignKey('amenities.id'),\
#                         primary_key=True, nullable=False)\
#                     )

class Amenity(BaseModel, Base):
    """ This class defines an amenity by various attributes
    """
    __tablename__ = 'amenities'
    if ENV_VAR['hbnb_storage_type'] == "db":
        name = Column(String(128), nullable=False)
        # place_amenities = relationship('Place', secondary=place_amenity,\
                                    # back_populates='places')
    else:
        name = ""

