#!/usr/bin/python3
""" Module that defines the User class, and inherits
from the BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """The class definition of the User Class that will inherit
    from the BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
