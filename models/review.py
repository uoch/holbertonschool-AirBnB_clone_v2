#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    place_id = Column(String(1024),  nullable=False)
    user_id = Column(String(60), ForeignKey("places.id"),  nullable=False)
    text = Column(String(60), ForeignKey("users.id"), nullable=False)
