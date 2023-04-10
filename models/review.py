#!/usr/bin/python3
"""Class representing a review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Details of a review of a place"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Construct a Review instance"""
        super().__init__(*args, **kwargs)
