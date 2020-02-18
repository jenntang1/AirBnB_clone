#!/usr/bin/python3
""" Unittest for User Class """
from unittest import TestCase
from models.base_model import BaseModel
from models.user import User
from tests.test_models.test_base_model import BaseModel_Test


class User_Test(BaseModel_Test):
    """ Creating class to test User class. """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs):
        self.test_class = User
        self.test_name = "User"

    def test_user(self):
        pass

    def test_email(self):
        pass

    def test_password(self):
        pass

    def test_fist_name(self):
        pass

    def test_last_name(self):
        pass

if __name__ == "__main__":
    unittest.main()
