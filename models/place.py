#!/usr/bin/python3
""" Place Module for HBNB project """
from models.config import ENV_VAR
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity

# from .amenity import Amenity
# metadata = Base.metadata
# place_amenity = Table('place_amenity', metadata,\
#                     Column('place_id', String(60), ForeignKey('places.id'),\
#                         primary_key=True, nullable=False),\
#                     Column('amenity_id', String(60), ForeignKey('amenities.id'),\
#                         primary_key=True, nullable=False)\
#                     )

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if ENV_VAR['hbnb_storage_type'] == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', back_populates='place',
                           cascade="all, delete-orphan")
        # amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """Getter attribute amenities that returns a list of Amenity instances based on
            the attribute amenity_ids that contains all Amenity.id linked to the Place

            Returns:
                list: A list of Amenity instances linked to this Place
            """
            from models.__init__ import storage
            all_amenities = list(storage.all(Amenity).values())
            place_amenities = []
            place_amenities.append(a for a in all_amenities\
                if a.amenity_id in self.amenity_ids)
            return place_amenities

        @amenities.setter
        def amenities(self, obj):
            if obj is not None and isinstance(obj, Amenity):
                self.amenity_ids.append(obj.amenity_id)
