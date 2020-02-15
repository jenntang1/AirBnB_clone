#!/usr/bin/python3
""" Amenity Class Implementation / Importing BaseModel """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Subclass that inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        """ Implementing __init__ method as the constructor.
        Args:
            args: positional command line args
            kwargs: keyword command line args
        Attributes:
            ----------- public class attributes -----------
            name: empty string
        """
        super(Amenity, self).__init__(*args, **kwargs)
        self.name = ""
