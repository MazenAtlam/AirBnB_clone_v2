#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from .config import ENV_VAR


if (ENV_VAR['hbnb_storage_type'] == 'db'):
        from .engine.db_storage import DBStorage
        storage = DBStorage()
else:
        from .engine.file_storage import FileStorage
        storage = FileStorage()

storage.reload()
