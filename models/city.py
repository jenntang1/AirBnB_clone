#!/usr/bin/python3
""" City Class Implementation / Importing BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ Subclass that inherits from BaseModel
    Attributes:
        ----------- public class attributes -----------
        state_id: empty string but will be State.id
        name: empty string
    """
    state_id = ""
    name = ""
