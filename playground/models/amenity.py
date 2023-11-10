#!/usr/bin/python3
""" Module that defines the Amenity class, and inherits
from the BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """The class definition of the Amenity Class that will inherit
    from the BaseModel"""
    name = ""
