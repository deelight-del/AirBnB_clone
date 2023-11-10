#!/usr/bin/python3
""" Module that defines the Review class, and inherits
from the BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The class definition of the Review Class that will inherit
    from the BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
