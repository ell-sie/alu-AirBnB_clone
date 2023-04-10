#!/usr/bin/python3
""" test models for dictionary """
import unittest
from models.base_model import BaseModel
import datetime


class TestCaseBaseModelWithKwarg(unittest.TestCase):

    def setUp(self):
        """ base setup for everything """
        self.my_model = BaseModel()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        # print(self.id)
        # print(self.my_model)
        # print(type(self.my_model.created_at))
        # print("--")
        my_model_json = self.my_model.to_dict()
        # print(my_model_json)
        # print("JSON of my_model:")
        # for key in my_model_json.keys():
        #    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

        # print("--")
        self.my_new_model = BaseModel(**my_model_json)
        # print(self.my_new_model.id)
        # print(self.my_new_model)
        # print(type(self.my_new_model.created_at))

        # print("--")
        # print(self.my_model is self.my_new_model)

    def test_NewModel(self):
        """ checking to ensure instances are different
        objects """
        self.assertNotEqual(self.my_model, self.my_new_model)

    def test_idDifferentModels(self):
        """ ensuring the id are the same
        since the same object data was used to create it """
        self.assertEqual(self.my_model.id, self.my_new_model.id)

    def test_NewModelType(self):
        """ ensuring instance method is same as
        BaseModel"""
        self.assertEqual(self.my_new_model.__class__.__name__, "BaseModel")

    def test_dateFormatsCreated_at(self):
        """ ensuring the new created times are in
        date time format"""
        self.assertEqual(type(self.my_new_model.__dict__['created_at']), datetime.datetime)

    def test_dateFormatsUpdated_at(self):
        """ ensuring the new updated time are in
        date time format """
        self.assertEqual(type(self.my_new_model.__dict__['updated_at']), datetime.datetime)

    def test_CustomNameSet(self):
        """ ensuring custom name set for model
        is still the same """
        self.assertEqual(self.my_new_model.__dict__['name'], "My_First_Model")

    def test_CustomNumberSet(self):
        """ensuring the right custom number is set
        """
        self.assertEqual(self.my_model.__dict__['my_number'], 89)


if __name__ == '__main__':
    unittest.main()


"""
import unittest


class TestCaseBaseModel(unittest.TestCase):

    def test_setup(self):
        from models.base_model import BaseModel

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        print(my_model.id)
        print(my_model)
        print(type(my_model.created_at))
        print("--")
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

        print("--")
        my_new_model = BaseModel(**my_model_json)
        print(my_new_model.id)
        print(my_new_model)
        print(type(my_new_model.created_at))

        print("--")
        print(my_model is my_new_model)
"""

