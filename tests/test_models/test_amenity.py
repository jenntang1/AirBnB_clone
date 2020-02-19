#!/usr/bin/python3
""" Unittest for Amenity Class """
from models.amenity import Amenity
from tests.test_models.test_base_model import BaseModel_Test


class Amenity_Test(BaseModel_Test):
    """ Creating class to test Amenity class. """
    def __init__(self, *args, **kwargs):
        """ Using __init__ method """
        super().__init__(*args, **kwargs)
        self.test_class = Amenity

    def test_amenity_name(self):
        """ Check name type """
        test = self.test_class()
        self.assertIsInstance(test.name, str)
