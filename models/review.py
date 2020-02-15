#!/usr/bin/python3
""" Review Class Implementation / Importing BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Subclass that inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        """ Implementing __init__ method as the constructor.
        Args:
            args: positional command line args
            kwargs: keyword command line args
        Attributes:
            ----------- public class attributes -----------
            place_id: empty string but will be Place.id
            user_id: empty string but will be User.id
            text: empty string
        """
        super(Review, self).__init__(*args, **kwargs)
        self.place_id = kwargs.get("place_id")
        self.user_id = kwargs.get("user_id")
        self.text = ""
