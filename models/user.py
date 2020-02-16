#!/usr/bin/python3
""" User Class Implementation / Importing BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Subclass that inherits from BaseModel
    Attributes:
       ----------- public class attributes -----------
       email: empty string
       password: empty string
       first_name: empty string
       last_name: empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
