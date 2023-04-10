#!/usr/bin/python3
""" Import BaseModel class from models/base_model.py """
from models.base_model import BaseModel
""" Define State class that inherits from BaseModel """


class State(BaseModel):
    """Class variable to store state name"""
    name = ""
