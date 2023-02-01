#!/usr/bin/python3
"""Test Place"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class TestPlace(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that the code follows PEP8 style guidelines."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        """test instance."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_class_name(self):
        """Test the name of the class."""
        place = Place()
        self.assertEqual(place.__class__.__name__, "Place")

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        place = Place()
        self.assertTrue(issubclass(place.__class__, BaseModel))

    def test_attributes(self):
        """Test the attributes of the Place class."""
        city = City()
        user = User()
        amenity = Amenity()
        place = Place()
        place.city_id = city.id
        place.user_id = user.id
        place.name = ""
        place.description = ""
        place.number_rooms = 0
        place.number_bathrooms = 0
        place.max_guest = 0
        place.price_by_night = 0
        place.latitude = 0.0
        place.longitude = 0.0
        place.amenity_ids = [amenity.id]
        self.assertEqual(place.city_id, city.id)
        self.assertEqual(place.user_id, user.id)
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertIsInstance(place.number_rooms, int)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertEqual(place.max_guest, 0)
        self.assertIsInstance(place.max_guest, int)
        self.assertEqual(place.price_by_night, 0)
        self.assertIsInstance(place.price_by_night, int)
        self.assertEqual(place.latitude, 0.0)
        self.assertIsInstance(place.latitude, float)
        self.assertEqual(place.longitude, 0.0)
        self.assertIsInstance(place.longitude, float)
        self.assertEqual(place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
