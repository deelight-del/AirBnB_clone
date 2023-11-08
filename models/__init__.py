#!/usr/bin/python3
""" This module is used to link the BaseModel and the
File Storage together."""
from models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
