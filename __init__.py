#!/usr/bin/python3
import models
from models.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()


__class__ = BaseModel()
