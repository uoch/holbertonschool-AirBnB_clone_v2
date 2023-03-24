#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    __tablename__ = 'cities'
    """ The city class, contains state ID and name """
    state_id = Column(String(60),  ForeignKey("state_id"), nullable=False)
    name = Column(String(128), nullable=False)
