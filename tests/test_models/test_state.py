#!/usr/bin/python3
"""test the state"""
import unittest
import pep8
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """Tes the state class"""

def test_instance(self):
        """test instance."""
        state = State()
        self.assertIsInstance(state, State)

def test_inheritance(self):
        """test is_subclass."""
        state = State()
        self.assertTrue(issubclass(type(state), BaseModel))

def test_pep8_conformance(self):
      """Test that we conform to PEP8."""
      pep8style = pep8.StyleGuide(quiet=True)
      result = pep8style.check_files(['models/state.py'])
      self.assertEqual(result.total_errors, 0, "Found code style errors.")

def test_class(self):
    state = State()
    self.assertEqual(state.__class__.__name__, "State")

def test_state_name(self):
    state = State()
    state.name = ""
    self.assertEqual(state.name, '')


if __name__ == "__main__":
    unittest.main()
