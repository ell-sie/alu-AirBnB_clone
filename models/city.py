#!/usr/bin/python3
"""City class definition"""

from models.base_model import BaseModel


class City(BaseModel):
    """Define City class"""
    state_id = ""
    name = ""

    """Constructor for the class"""

    def __init__(self, *args, **kwargs):
        """Call parent constructor"""
        super().__init__(*args, **kwargs)
