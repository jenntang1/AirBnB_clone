#!/usr/bin/python3
""" BaseModel Implementation """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Parent/Base class that defines all common/public
    attributes and methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """ Implementing __init__ method as the constructor.
        Args:
            args: positional command line args; not used
            kwargs: keyword command line args
        Attributes:
            id: unique id converted into a string
            created_at: current datetime
            updated_at: updated datetime
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if (len(kwargs) > 0) and (kwargs is not None):
            self.__dict__ = kwargs
            self.__dict__['created_at'] = datetime.strptime
            (self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__['updated_at'] = datetime.strptime
            (self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """ Implementing __str__ method for string
        representation of an object.
        Returns:
            [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """ Creating public instance method that
        updates updated_at with current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Creating public instance method that
        returns a dictionary representation of BaseModel.
        Returns:
            new dictionary
        """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
