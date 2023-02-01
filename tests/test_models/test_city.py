#!/usr/bin/python3
"""test city."""
import unittest
from models.city import City
from models.state import State 
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test the City class."""

    def test_pep8_conformance_city(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


    def test_instance(self):
        """test instance."""
        city = City()
        self.assertIsInstance(city, City)

    def test_class(self):
        city = City()
        self.assertEqual(str(type(city)),
                         "<class 'models.city.City'>")

    def test_inheritance(self):
        """test inheritance."""
        city = City()
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_city(self):
        """
        Test attributes of Class City
        """
        my_city = City()
        my_state = State()
        my_city.name = ""
        my_city.state_id = my_state.id
        self.assertEqual(my_city.name, '')
        self.assertEqual(my_city.state_id, my_state.id)


if __name__ == "__main__":
    unittest.main()