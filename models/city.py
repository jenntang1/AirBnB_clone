#!/usr/bin/python3
""" City Class Implementation / Importing BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ Subclass that inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        """ Implementing __init__ method as the constructor.
        Args:
            args: positional command line args
            kwargs: keyword command line args
        Attributes:
            ----------- public class attributes -----------
            state_id: empty string but will be State.id
            name: empty string
        """
        super(City, self).__init__(*args, **kwargs)
        self.state_id = kwargs.get("state_id")
        self.name = ""
