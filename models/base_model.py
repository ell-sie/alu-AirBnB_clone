#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    """The BaseModel class"""
    def __init__(self, *args, **kwargs):
        """the class constructor"""
        """args to take any arguments and kwargs for pairs/key(dict)"""

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

        if kwargs != 0:
            for x, y in kwargs.items():
                """kwargs.items() helps to read the arguments names and values"""
                if x != '__class__':
                    if x == 'created_at'or 'updated_at':
                        self.__dict__[x] = datetime.strptime(y, time_format)
                    else:
                        self.__dict__[x] = y
        else:
           self.id = str(uuid.uuid4())
           self.created_at = datetime.datetime.today() 
           
    def __str__(self):
        """displaying the class name"""
        return '[{}] ({}) <{}>'\
            .format(self.__class__.__name__, self.id, self.__dict__)
        """print('[{}] ({}) <{}>'.format(type().__name__, self.id, self.__dict__))"""
    def save(self):
        print(str(self.updated_hour) +":"+ str(self.updated_at.minute))
        storage.save(self)
    
    def to_dict(self):
        """return dictionary of the class instance"""
        fdict = self.__dict__.copy()
        fdict["created_at"] = (self.created_at.isoformat())
        fdict["update_at"] = (self.updated_at.isoformat())
        fdict["__class__"] = self.__class__.__name__
        return fdict

