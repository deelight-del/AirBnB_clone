#!/usr/bin/pyhton3
""" This module contains the class definition of
the BaseModel that will later be inherited by other classes
in our entire program"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Class definition of the BaseModel with some public instance
    attributes, and some public instance methods"""
    def __init__(self, *args, **kwargs):
        """The special method init that is called whenever a new instance
        is created.

        Args:
            args - variable length arguments.
            kwargs - variable length key worded arguments

        Return:
            Nothing.
        """
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k == "created_at" or k == "updated_at":
                    date_value = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, date_value)
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """The magic method that is used by the print function to print out
        an object.

        Args:
            self: Object reference.

        Return:
            A String that is used by the print function to print some value.
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """This method updates the `updated_at` public attribute of
        the instance with the current date and time, as a datetime object.
        """
        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """The method returns the dictionary containing the keys/values
        of __dict__ of the instance with some little mods, such as adding
        the __class__ key and the respective class name as key."""
        instance_dict = {}
        instance_dict["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                instance_dict[k] = v.isoformat()
            else:
                instance_dict[k] = v
        return instance_dict
