#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          back_populates="state",
                          cascade="all, delete-orphan")
    # @property
   # def cities(self):
       # from models import storage
       # list_of_cities = []
        # for city in DB.__session.query(State).
        # filter(State.id == City.state_id): 
        # list_of_cities.append(city)
