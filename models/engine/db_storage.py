#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from models.config import ENV_VAR
from sqlalchemy.orm import sessionmaker, scoped_session
from ..state import State
from ..city import City
from ..user import User
from ..amenity import Amenity
from ..place import Place
from ..review import Review
from sqlalchemy import create_engine
from ..base_model import Base


class DBStorage:
    """This class manages storage of hbnb models in tables"""

    classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }

    __engine = None
    __session = None
    def __init__(self):
            self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                          .format(ENV_VAR['hbnb_usr'], ENV_VAR['hbnb_usr_pwd'],
                                                  ENV_VAR['hbnb_host'], ENV_VAR['hbnb_db'])
                                          , pool_pre_ping=True)
            if ENV_VAR['hbnb_env'] == 'test':
                Base.metadate.drop_all(self.__engine)

    def all(self, cls=None):
        """
        querying a specific table in the db if cls is specified
        Otherwise all tables in db is queried
        """
        temp_dict = {}

        if cls is not None:
            if isinstance(cls, str):
                print(cls)
                cls = globals().get(cls)
                print(cls)

            for obj in self.__session.query(cls):
                temp_dict.update({f"{cls.__name__}.{obj.id}" : obj})
        else:
            for value in DBStorage.classes.values():
                for obj in self.__session.query(value).all():
                    temp_dict.update({f"{value.__name__}.{obj.id}" : obj})
        return temp_dict

    def new(self, obj):
        """
        add obj to current db session
        """
        obj = self.__session.merge(obj)
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """
        commit all changes in th current db session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete obj from the current db session
        """
        if obj is not None:
            self.__session.delete(obj)
            self.save(self)

    def reload(self):
        """
        Create All Tables in the db
        Create Current db session
        """
        Base.metadata.create_all(self.__engine)
        session_factory =  sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
