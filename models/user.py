#!/usr/bin/python3
""" User Class Implementation / Importing BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Subclass that inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        """ Implementing __init__ method as the constructor.
        Args:
            args: positional command line args
            kwargs: keyword command line args
        Attributes:
            ----------- public class attributes -----------
            email: empty string
            password: empty string
            first_name: empty string
            last_name: empty string
        """
        super(User, self).__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
