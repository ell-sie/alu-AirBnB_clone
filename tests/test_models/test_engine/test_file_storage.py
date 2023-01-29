#!/usr/bin/python
"""test for the file storage"""
import unittest
import os
import pep8
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.path = "file.json"
        
    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_all(self):
        """Tests if the all method returns a dictionary"""
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        
    def test_new(self):
        """Tests if a new object is added to the dictionary"""
        user = User()
        user.id = "123456"
        user.name = "Leon"
        self.storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(self.storage.all()[key])
        
    def test_reload(self):
        """Tests if the reload method reloads the dictionary from the file"""
        self.storage.save()
        os.remove("file.json")
        self.storage.save()
        with open("file.json", "w") as f:
            f.write("{}")
        self.assertIsNone(self.storage.reload())

