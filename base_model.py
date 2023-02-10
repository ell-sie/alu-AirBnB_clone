#!/usr/bin/python
import models
import uuid
import datetime


class BaseModel:
    """The BaseModel class"""
    def __init__(self, *args, **kwargs):
        """the class constructor and takes kwargs"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs != 0:
            for key, value in kwargs.items():
                """kwargs.items() to read args names and vals"""
                if key != '__class__':
                    if key == 'created_at' or 'updated_at':
                        self.__dict__[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()

    def __str__(self):
        """displaying the class name"""
        classname = self.__class__.__name__
        return '[{}] ({}) <{}>'\.format(self.__class__.__name__, self.id, self.__dict__)
        
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        wdict = self.__dict__.copy()
        wdict["__class__"] = self.__class__.__name__
        wdict["created_at"] = self.created_at.isoformat()
        wdict["updated_at"] = self.updated_at.isoformat()
        return wdict
