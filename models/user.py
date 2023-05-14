#!/usr/bin/python3
"""The console , user module"""

from models.base_model import BaseModel


class User(BaseModel):
    """attributes and methods for the class inherited from the BaseModel class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
