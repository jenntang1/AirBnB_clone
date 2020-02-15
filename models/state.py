#!/usr/bin/python3
""" State Class Implementation / Importing BaseModel """
from models.base_model import BaseModel


class State(BaseModel):
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
        super(State, self).__init__(*args, **kwargs)
        self.name = ""
