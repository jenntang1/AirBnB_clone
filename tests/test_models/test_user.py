#!/usr/bin/python3
""" Unittest for User Class """
from unittest import TestCase
from models.base_model import BaseModel
from models.user import User
from test.testmodels.test_base_model import TestBaseModel


class User_Test(TestBaseModel):
    """ Creating class to test User class. """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs):

if __name__ == "__main__":
    unittest.main()
