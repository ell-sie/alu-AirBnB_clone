#!/usr/bin/python3
import models
from models.base_model import BaseModel
import json

class FileStorage:
    __file_path : str
    __objects : dict

    def all(self):
        return __objects

    def new(self, obj):
        __objects = self.obj{'__class__': '.id'}

    def save(self):
        "__file_path": [{'__objects']}

    def reload(self):
        if __objects in __file_path:
            return __objects
        else:
            return 0
