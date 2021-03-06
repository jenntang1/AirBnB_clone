#!/usr/bin/python3
""" BaseModel Implementation """
import uuid
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
        if (len(kwargs) > 0) and (kwargs is not None):
            updt = self.__dict__
            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            updt.update(kwargs)
            updt['created_at'] = datetime.strptime(self.created_at, fmt)
            updt['updated_at'] = datetime.strptime(self.updated_at, fmt)
            del updt['__class__']
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

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
