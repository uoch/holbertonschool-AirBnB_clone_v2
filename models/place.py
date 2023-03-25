#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, INTEGER, Float, Table
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import relationship
from os import getenv
metadata = Base.metadata
place_amenity_table = Table('place_amenity',
                            metadata, Column('place_id', String(60),
                                             ForeignKey(
                                'places.id'),
                                primary_key=True, nullable=False),
                            Column('amenity_id', String(60),
                                   ForeignKey('amenities.id'),
                                   primary_key=True, nullable=False))


class Place(BaseModel):
    """ A place to stay """
	__tablename__ = 'places'
    city_id = Column(String(60),  ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60),  ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(INTEGER, nullable=False, default=0)
    number_bathrooms = Column(INTEGER, nullable=False, default=0)
    max_guest = Column(INTEGER, nullable=False, default=0)
    price_by_night = Column(INTEGER, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    