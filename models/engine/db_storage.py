#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        db = os.getenv('HBNB_MYSQL_DB')
        host = os.getenv("HBNB_MYSQL_HOST")
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{db}",
            pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries on the database session"""
        objects = {}
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            if type(cls) == str:
                classes = eval(cls)
            else:
                classes = cls
        for cls_ in classes:
            for obj in self.__session.query(cls_).all():
                objects[f"{type(obj).__name__}.{obj.id}"] = obj
        return objects

    def new(self, obj):
        """Adds an object to the database sessiom"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object (if not None) from the database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the DB
        Create the current DB session from the engine
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(session)
        self.__session = session()
