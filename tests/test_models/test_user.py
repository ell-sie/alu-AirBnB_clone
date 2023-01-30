#!/usr/bin/python3
import unittest
import pep8
from models.user import User

class TestUser(unittest.TestCase):


    def test_pep8_conformance(self):
     """Test that the code conforms to PEP8 guidelines"""
    pep8style = pep8.StyleGuide(quiet=True)
    result = pep8style.check_files(['models/user.py'])
    self.assertEqual(result.total_errors, 0, "Code does not conform to PEP8")


    def test_attributes(self):
     """Test the attributes of the User class"""
    user = User()
    user.first_name = 'Agasaro'
    user.last_name = 'Elsie'
    user.email = 'ag@alustudent.com'
    self.assertEqual(user.first_name, 'Agasaro')
    self.assertEqual(user.last_name, 'Elsie')
    self.assertEqual(user.email, 'ag@alustudent.com')
