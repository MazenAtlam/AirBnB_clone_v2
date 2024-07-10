#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from datetime import datetime
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    date, time = value.split('T')
                    yy, mm, dd = map(int, date.split('-'))
                    hh, MM, ss_ms = time.split(':')
                    hh = int(hh)
                    MM = int(MM)
                    ss, ms = map(int, ss_ms.split('.'))
                    value = datetime(yy, mm, dd, hh, MM, ss, ms)

                self.__setattr__(key, value)
        else:
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        self.__dict__.pop("_sa_instance_state")
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if dictionary.get("_sa_instance_state") is not None:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """Delete Current Instance from the storage"""
        from models import storage
        storage.delete(self)
