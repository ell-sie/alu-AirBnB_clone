#!/usr/bin/env python3
"""Test Review"""

import unittest
import pep8
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.user import User


class TestReview(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         f"Found {result.total_errors} code style errors (and warnings).")

    def test_class(self):
        review = Review()
        self.assertEqual(review.__class__.__name__, "Review")

    def test_inheritance(self):
        review = Review()
        self.assertTrue(issubclass(review.__class__, BaseModel))

    def test_attributes(self):
        """Test the 'place_id', 'user_id', and 'text' attributes of the Review class."""
        place = Place()
        user = User()
        review = Review()
        review.place_id = place.id
        review.user_id = user.id
        review.text = ''
        self.assertEqual(review.place_id, place.id, '')
        self.assertEqual(review.user_id, user.id, '')
        self.assertEqual(review.text, '')


if __name__ == "__main__":
    unittest.main()
