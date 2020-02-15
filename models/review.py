#!/usr/bin/python3
""" Review Class Implementation / Importing BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Subclass that inherits from BaseModel
    Attributes:
        ----------- public class attributes -----------
        place_id: empty string but will be Place.id
        user_id: empty string but will be User.id
        text: empty string
    """
    self.place_id = ""
    self.user_id = ""
    self.text = ""
