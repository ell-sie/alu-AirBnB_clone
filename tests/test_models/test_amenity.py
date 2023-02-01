#!/usr/bin/env python3
"""Test Amenity"""

import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class TestAmenity(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         f"Found {result.total_errors} code style errors (and warnings).")

    def test_class(self):
        amenity = Amenity()
        self.assertEqual(amenity.__class__.__name__, "Amenity")

    def test_inheritance(self):
        amenity = Amenity()
        self.assertTrue(issubclass(amenity.__class__, BaseModel))

    def test_attribute(self):
        """Test the 'name' attribute of the Amenity class."""
        my_amenity = Amenity()
        my_amenity.name = "Wi-Fi"
        self.assertEqual(my_amenity.name, 'Wi-Fi')
