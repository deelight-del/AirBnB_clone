#!/usr/bin/python3
""" Module that defines the Place class, and inherits
from the BaseModel"""

from models.base_model import BaseModel


class Place(BaseModel):
    """The class definition of the Place Class that will inherit
    from the BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []
