#!/usr/bin/python3
""" BaseModel Implementation """
import uuid
import datetime


class BaseModel:
    """ Parent class that defines all common/public
    attributes and methods for other classes.
    """
    def __init__(self):
        """ Implementing __init__ method.
        Attributes:
            id: unique id converted into a string
            created_at: current datetime
            updated_at: updated datetime
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ Implementing __str__ method for string
        representation of an object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Creating public instance method that
        updates updated_at with current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Creating public instance method that
        returns a dictionary of __dict__.
        """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
