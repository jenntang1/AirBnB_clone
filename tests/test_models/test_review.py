#!/usr/bin/python3
""" Unittest for Review Class """
from tests.test_models.test_base_model import BaseModel_Test
from models.review import Review


class Review_Test(BaseModel_Test):
    """ Creating class to test Review class. """
    def __init__(self, *args, **kwargs):
        """ Using __init__ method """
        super().__init__(*args, **kwargs)
        self.test_class = Review

    def test_place_id(self):
        """ Check place_id type """
        test = self.test_class()
        self.assertIsInstance(test.place_id, str)

    def test_user_id(self):
        """ Check user_id type """
        test = self.test_class()
        self.assertIsInstance(test.user_id, str)

    def test_text(self):
        """ Check text type """
        test = self.test_class()
        self.assertIsInstance(test.text, str)
