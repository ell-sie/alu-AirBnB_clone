#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    """The BaseModel class"""
    def __init__(self, id, created_at, updated_at):
        """the class constructor"""
        self.id = uuid.uuid4()
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__ = '__class__'
        self.__dict__['created_at'] = datetime.datetime.strptime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
        self.__dict__['updated_at'] = datetime.datetime.strptime(self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
        return self.__dict__
