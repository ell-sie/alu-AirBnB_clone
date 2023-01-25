#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.now()

    def __str__(self):
        print(id.__class__.__name__)
        print(self.id)
        print(self.__dict__)
    def save(self):
        print(str(self.updated_hour) +":"+ str(self.updated_at.minute))
    
    def to_dict(self):
        print(self.created_at.isoformat())
        print(self.updated_at.isoformat())
