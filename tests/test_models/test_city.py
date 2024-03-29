#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCaseCity(unittest.TestCase):
    """Test case for City class."""

    def test_instance(self):
        """Test instantiation of class."""
        city = City()
        self.assertIsInstance(city, City)

    def test_is_class(self):
        """Test instance."""
        city = City()
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")

    def test_is_subclass(self):
        """Test if City is_subclass of BaseModel."""
        city = City()
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_state_id(self):
        """Test state_id attribute."""
        city = City()
        self.assertEqual(city.state_id, "")
        city.state_id = "kigali"
        self.assertEqual(city.state_id, "kigali")

    def test_name(self):
        """Test name of attribute."""
        city = City()
        self.assertEqual(city.name, "")
        city.name = "bali"
        self.assertEqual(city.name, "bali")
        self.assertIsNotNone(city.id)

    if __name__ == "__main__":
        unittest.main()
