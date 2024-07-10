#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column, ForeignKey, Integer


class Review(BaseModel , Base):
    """ Review classto store review information """

    __tablename__ = 'reviews'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    place_id = Column(String(60), ForeignKey('places.id'))
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
    # user = relationship('User', back_populates='reviews')
    # place = relationship('Place', back_populates='reviews')
