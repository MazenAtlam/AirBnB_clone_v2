#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from .config import ENV_VAR
from models.engine.file_storage import FileStorage
if (ENV_VAR['hbnb_storage_type'] == 'db'):
        from .engine.db_storage import DBStorage
        storage = DBStorage()
        storage.reload()
elif (ENV_VAR['hbnb_storage_type'] == 'file'):
        from .engine.file_storage import FileStorage
        storage = FileStorage()
        storage.reload()
