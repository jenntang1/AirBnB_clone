#!/usr/bin/python3
""" Unittest for User Class """
from models.user import User
from tests.test_models.test_base_model import BaseModel_Test


class User_Test(BaseModel_Test):
    """ Creating class to test User class. """
    def __init__(self, *args, **kwargs):
        """ Using __init__ method """
        super().__init__(*args, **kwargs)
        self.test_class = User

    def test_email(self):
        """ Check email type """
        test = self.test_class()
        self.assertIsInstance(test.email, str)

    def test_password(self):
        """ Check password type """
        test = self.test_class()
        self.assertIsInstance(test.password, str)

    def test_first_name(self):
        """ Check first_name type """
        test = self.test_class()
        self.assertIsInstance(test.first_name, str)

    def test_last_name(self):
        """ Check last_name type """
        test = self.test_class()
        self.assertIsInstance(test.last_name, str)

if __name__ == "__main__":
    unittest.main()
