#!/usr/bin/python3
"""Test Place"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User


class Testplace(unittest.TestCase):

    def test_is_nstance(self):
        """test instance."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_pep8_conformance_place(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        place1 = Place()
        self.assertEqual(place1.__class__.__name__, "Place")

    def test_inheritance(self):
        place1 = Place()
        self.assertTrue(issubclass(place1.__class__, BaseModel))

    def test_place(self):
        """
        Test attributes of Class Place
        """
        my_amenity = Amenity()
        my_city = City()
        my_user = User()
        my_place = Place()
        my_place.city_id = City.id
        my_place.user_id = User.id
        my_place.name = ''
        my_place.description = ''
        my_place.number_rooms = 0
        my_place.number_bathrooms = 0
        my_place.max_guest = 0
        my_place.price_by_night = 0
        my_place.latitude = 0.0
        my_place.longitude = 0.0
        my_place.amenity_ids = str(my_amenity.id)
        self.assertEqual(my_place.city_id, my_city.id)
        self.assertEqual(my_place.user_id, my_user.id)
        self.assertEqual(my_place.name, '')
        self.assertEqual(my_place.description, '')
        self.assertEqual(my_place.number_rooms, 0)
        self.assertTrue(type(my_place.number_rooms), int)
        self.assertEqual(my_place.number_bathrooms, 0)
        self.assertTrue(type(my_place.number_bathrooms), int)
        self.assertEqual(my_place.max_guest, 0)
        self.assertTrue(type(my_place.max_guest), int)
        self.assertEqual(my_place.price_by_night, 0)
        self.assertTrue(type(my_place.price_by_night), int)
        self.assertEqual(my_place.latitude, 0.0)
        self.assertTrue(type(my_place.latitude), float)
        self.assertEqual(my_place.longitude, 0.0)
        self.assertTrue(type(my_place.longitude), float)
        self.assertEqual(my_place.amenity_ids, str(my_amenity.id))
        self.assertTrue(type(my_place.amenity_ids), str)