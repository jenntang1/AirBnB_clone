#!/usr/bin/python3
""" State Class Implementation / Importing BaseModel """
from models.base_model import BaseModel


class State(BaseModel):
    """ Subclass that inherits from BaseModel
    Attributes:
        ----------- public class attributes -----------
        name: empty string
    """
    name = ""
