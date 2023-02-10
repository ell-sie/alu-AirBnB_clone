#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    """The BaseModel class"""
    def __init__(self, *args, **kwargs):
        """the class constructor and takes kwargs"""
        self.id = uuid.uuid4()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

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
        return '[{}] ({}) <{}>'\.format(self.__class__.__name__, self.id, self.__dict__)
        
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__ = '__class__'
        self.__dict__['created_at'] = datetime.datetime.strptime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
        self.__dict__['updated_at'] = datetime.datetime.strptime(self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
        return self.__dict__
