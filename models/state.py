#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if storage_type != 'db':
        name = ""
    else:
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")

# cannot have cities attribute and getter attribute named cities along side, throws up error except backref instead of bak_populates is used
    if storage_type != 'db':
        @property
        def cities(self):
            """ returns list of
            city instances"""
            from models import storage
            list_of_cities = []
            for city_id, city_cls in storage.all(City).items():
                if self.id == city_cls.state_id:
                    list_of_cities.append(city_cls)
            return (list_of_cities)
