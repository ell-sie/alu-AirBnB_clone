#!/usr/bin/python3
""" test reload user """
from models import storage
from models.base_model import BaseModel
from models.user import User
import unittest


class TestCaseUser(unittest.TestCase):

    def setUp(self):
        """ user test setup """
        all_objs = storage.all()
        # print("-- Reloaded objects --")
        # for obj_id in all_objs.keys():
        #   obj = all_objs[obj_id]
        #   print(obj)

    def test_variables(self):
        """ test name before and after """
        # print("-- Create a new User --")
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()
        self.assertEqual(my_user.first_name, "Betty")
        self.assertEqual(my_user.last_name, "Bar")
        self.assertEqual(my_user.email, "airbnb@mail.com")
        self.assertEqual(my_user.password, "root")


"""
from models import storage
from models.base_model import BaseModel
from models.user import User
import unittest


class TestCaseUser(unittest.TestCase):

    def test_setup(self):
        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)

        print("-- Create a new User --")
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()
        print(my_user)

        print("-- Create a new User 2 --")
        my_user2 = User()
        my_user2.first_name = "John"
        my_user2.email = "airbnb2@mail.com"
        my_user2.password = "root"
        my_user2.save()
        print(my_user2)
"""
