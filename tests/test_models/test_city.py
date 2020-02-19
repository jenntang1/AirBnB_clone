#!/usr/bin/python3
""" Unittest for City Class """
from tests.test_models.test_base_model import BaseModel_Test
from models.city import City


class City_Test(BaseModel_Test):
    """ Creating class to test City class. """
    def __init__(self, *args, **kwargs):
        """ Using __init__ method """
        super().__init__(*args, **kwargs)
        self.test_class = City

    def test_state_id(self):
        """ Check state_id type """
        test = self.test_class()
        self.assertIsInstance(test.state_id, str)

    def test_city_name(self):
        """ Check name type """
        test = self.test_class()
        self.assertIsInstance(test.name, str)
