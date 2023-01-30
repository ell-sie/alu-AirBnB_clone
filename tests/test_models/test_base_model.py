#!/usr/bin/python3
""" test model for main base class"""
import unittest
from time import sleep
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()
        self.model.name = "My primary Model"
        self.model.my_number = 89

    def test_name(self):
        self.model.save()
        self.assertEqual(self.model.name, "My primary Model")

    def test_number(self):
        self.assertEqual(self.model.my_number, 89)

    def test_class(self):
        self.assertEqual(self.model.__class__.__name__, 'BaseModel')

    def test_dict_conversion(self):
        self.assertEqual(type(self.model.to_dict()), dict)

    def test_created_at(self):
        model_dict = self.model.to_dict()
        self.assertEqual(type(model_dict['created_at']), str)

    def test_updated_at(self):
        model_dict = self.model.to_dict()
        self.assertEqual(type(model_dict['updated_at']), str)

    def test_save_updates_time(self):
        old_time = self.model.to_dict()['updated_at']
        sleep(2)
        self.model.save()
        self.assertNotEqual(self.model.to_dict()['created_at'],
                            self.model.to_dict()['updated_at'])

    def test_id_consistency(self):
        self.model.save()
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['id'], self.model.__dict__['id'])

    def test_dict_size(self):
        self.assertEqual(len(self.model.to_dict()), len(self.model.__dict__) + 1)
