#!/usr/bin/python3
"""Test the user"""
import unittest
import pep8
from models.city import City
from models.amenity import Amenity
from models.base_model import Basemodel
from models.place import Place
from models.user import User 
from models.review import Review
from models.state import State


class TestUser(unittest.TestCase):
    def test_pep8_conformance(self):
    """Test that the code conforms to PEP8."""
    pep8style = pep8.StyleGuide(quiet=True)
    result = pep8style.check_files(['models/user.py'])
    self.assertEqual(result.total_errors, 0,
                     "Found code style errors (and warnings).")

def test_user_attributes(self):
    """
    Test the attributes of the User class
    """
    my_user = User()
    my_user.first_name = 'John'
    my_user.last_name = 'Doe'
    my_user.email = 'johndoe@example.com'
    self.assertEqual(my_user.first_name, 'John')
    self.assertEqual(my_user.last_name, 'Doe')
    self.assertEqual(my_user.email, 'johndoe@example.com')
def test_pep8_conformance(self):
    """Test that the code conforms to PEP8."""
    pep8style = pep8.StyleGuide(quiet=True)
    result = pep8style.check_files(['models/user.py'])
    self.assertEqual(result.total_errors, 0,
                     "Found code style errors (and warnings).")

def test_user_attributes(self):
    """
    Test the attributes of the User class
    """
    my_user = User()
    my_user.first_name = 'John'
    my_user.last_name = 'Doe'
    my_user.email = 'johndoe@example.com'
    self.assertEqual(my_user.first_name, 'John')
    self.assertEqual(my_user.last_name, 'Doe')
    self.assertEqual(my_user.email, 'johndoe@example.com')



