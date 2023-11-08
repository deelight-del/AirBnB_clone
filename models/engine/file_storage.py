#!/usr/bin/python3
""" This module contains the class definition of the File
Storage class that will facilitate persisting the instances created
from respective Base Classes and others."""

import json
from models.base_model import BaseModel


class FileStorage:
    """Class definiton of the FileStorage for persisting
    instances of classes created"""
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """ The method used to return the private class attribute
        `__objects`"""
        return FileStorage.__objects

    def new(self, obj):
        """Instance method of the FileStorage that will save a new
        object intto the `__objects` dictionary

        Args:
            self - Instance/Object of FileStorage.
            obj - Object or instance to save.

        Return:
            None
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ This method serializes the __objects dictionary to a JSON
        file using the class attribute file_path"""
        object_dict = dict()
        if FileStorage.__objects:
            for k, v in FileStorage.__objects.items():
                object_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(object_dict, f)

    def reload(self):
        """ This method deserializes the JSON file to the class private
        attributes `FileStorage` """
        classes_dictionary = {"BaseModel": BaseModel}
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                dict_of_objects = json.load(f)
                for key, val in dict_of_objects.items():
                    object_class = classes_dictionary[val["__class__"]]
                    FileStorage.__objects[key] = object_class(**val)
        except FileNotFoundError:
            pass

    def reset(self, dictionary=dict()):
        """ The method that resets the dictionary to an
        empty dictionary

        Args:
            self: The instance refernce
            dictionary: The empty dictionary to initialize to.

        Return:
            Nothing.
        """
        FileStorage.__objects = dict()
