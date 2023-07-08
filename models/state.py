#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from os import getenv
import models

class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities