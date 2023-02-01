#!/usr/bin/python3
import unittest
import pep8
from models.user import User

class TestUser(unittest.TestCase):


    def test_instance(self):
        """test the instance."""
        user = User()
        self.assertIsInstance(user, User)

    
    def test_is_class(self):
        """test instance."""
        user = User()
        self.assertEqual(str(type(user)),
                         "<class 'models.user.User'>")


    def test_is_subclass(self):
        """test is_subclass."""
        user = User()
        self.assertTrue(issubclass(type(user), BaseModel))


    def test_id(self):
        """test email."""
        my_user = User()
        self.assertIsNotNone(my_user.id)


    def test_password(self):
        """test password."""
        my_user = User()
        self.assertEqual(my_user.password, "")
        my_user.password = "root"
        self.assertEqual(my_user.password, "root")


    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8 guidelines"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Code does not conform to PEP8")


    def test_attributes(self):
        """Test the attributes of the User class"""
        user = User()
        user.first_name = 'Betty'
        user.last_name = 'Bar'
        user.email = 'airbnb@mail.com'
        self.assertEqual(user.first_name, 'Betty')
        self.assertEqual(user.last_name, 'Bar')
        self.assertEqual(user.email, 'airbnb@mail.com')
