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
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

# cannot have cities attribute and getter attribute named cities along side, throws up error except backref instead of bak_populates is used
    @property
    def citiess(self):
        """ returns list of
        city instances"""
        from models.engine import FileStorage
        list_of_cities = []
        for key, value in FileStorage.all(City).items():
            if self.id == value.state_id:
                list_of_cities.append(value)
        return (list_of_cities)
