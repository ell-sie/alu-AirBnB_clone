#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return '[{}] ({}) <{}>'\
            .format(__class__.__name__, self.id, self.__dict__)
        """print('[{}] ({}) <{}>'.format(type().__name__, self.id, self.__dict__))"""
    def save(self):
        print(str(self.updated_hour) +":"+ str(self.updated_at.minute))
    
    def to_dict(self):
        print(self.created_at.isoformat())
        print(self.updated_at.isoformat())
