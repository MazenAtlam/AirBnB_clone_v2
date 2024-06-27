#!/usr/bin/python3
from console.HBNBCommand import config
from sqlalchemy import String, Column
from sqlalchemy.orm import sessionmaker, scoped_session
class DBStorage:
    classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }
    __engine = None
    __session = None
    def __init__(self):
            self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                          .format(config['hbnb_usr'], config['hbnb_usr_pwd'],
                                                  config['hbnb_host'], config['hbnb_db'])
                                          , pool_pre_ping=True)
            if config['hbnb_env'] == 'test':
                    # Drop All Tables
                    pass
    def all(self, cls=None):
        """
        querying a specific table in the db if cls is specified
        Otherwise all tables in db is queried
        """
        temp_dict = {}
        if cls is not None:
            for obj in self.__session.query(cls).all():
                temp_dict.update({f"{cls}.{obj.id}" : obj})
        else:
            for value in BStorage.classes.values():
                for obj in self.__session.query(value).all():
                    temp_dict.update({f"{value}.{obj.id}" : obj})
        return temp_dict

    def new(self, obj):
        """
        add obj to current db session
        """
        self.__session.add(obj)
    def save(self):
        """
        commit all changes in th current db seession
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
        from ..base_model import Base
        from ..state import State
        from ..city import City
        Base.metadata.create_all(self.__engine)
        session_factory =  sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

