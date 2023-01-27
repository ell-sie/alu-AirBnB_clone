#!/usr/bin/python3
"""Test console"""
import unittest
import pep8


class TestPep8(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that all files conform to PEP8."""
        files_to_check = ['models/amenity.py', 'models/base_model.py',
                          'models/city.py', 'models/place.py',
                          'models/review.py', 'models/state.py',
                          'models/user.py', 'models/__init__.py',
                          'models/engine/file_storage.py', 'console.py']
        pep8style = pep8.StyleGuide(quiet=True)
        for file in files_to_check:
            result = pep8style.check_files([file])
            self.assertEqual(result.total_errors, 0,
        f"Found code style errors (and warnings) in {file}.")
