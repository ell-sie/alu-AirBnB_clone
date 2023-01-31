#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    """The BaseModel class"""
    def __init__(self, id, created_at, updated_at):
        """the class constructor"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """displaying the class name"""
        """return '[{}] ({}) <{}>'\
            .format(self.__class__.__name__, self.id, self.__dict__)"""
        print('[{}] ({}) <{}>'.format(type().__name__, self.id, self.__dict__))

        def save(self):
            print(str(self.updated_hour) + ":" + str(self.updated_at.minute))

    def to_dict(self):
        """return dictionary of the class instance"""
        fdict = self.__dict__.copy()
        fdict["created_at"] = (self.created_at.isoformat())
        fdict["update_at"] = (self.updated_at.isoformat())
        fdict["__class__"] = self.__class__.__name__
        return fdict
