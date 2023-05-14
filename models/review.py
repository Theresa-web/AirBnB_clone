#!/usr/bin/python3
"""The console , Review module"""

from models.base_model import BaseModel

class Review(BaseModel):
    """attributes and methods for the class inherited from the BaseModel class"""

    place_id = ""
    user_id = ""
    text = ""
