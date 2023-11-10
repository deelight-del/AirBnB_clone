#!/usr/bin/python3
""" Module that defines the State class, and inherits
from the BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """The class definition of the State Class that will inherit
    from the BaseModel"""
    name = ""
