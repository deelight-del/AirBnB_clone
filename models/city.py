#!/usr/bin/python3
""" Module that defines the City class, and inherits
from the BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """The class definition of the City Class that will inherit
    from the BaseModel"""
    state_id = ""
    name = ""
