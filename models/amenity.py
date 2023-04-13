#!/usr/bin/python3
""" class for defining amenities.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class holds data on specific amenity """

    name = ""

    def __init__(self, *args, **kwargs):
        """ Set up an Amenity instance with its properties. """
        super().__init__(*args, **kwargs)
