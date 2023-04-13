#!/usr/bin/python3
"""Implementation of the review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Details of a review of a place"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Build a Review instance"""
        super().__init__(*args, **kwargs)
