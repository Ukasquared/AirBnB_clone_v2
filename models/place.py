#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from os import getenv
metadata = Base.metadata

storage_type = getenv("HBNB_MYSQL_DB")

place_amenity = Table('place_amenity', metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60),  ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60),  ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="places")
    reviews = relationship("Review", back_populates="place",
                           cascade="all, delete-orphan")
    amenities = relationship("Amenity", secondary=place_amenity, backref="place_amenities", viewonly=False)

    if storage_type == 'db':
        @property
        def amenities(self):
            pass

        @amenities.setter
        def amenities(self, amenity_obj):
            pass
