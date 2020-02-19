#!/usr/bin/python3
""" Unittest for Amenity Class """
from tests.test_models.test_base_model import BaseModel_Test
from models.amenity import Amenity


class Amenity_Test(BaseModel_Test):
    """ Creating class to test Amenity class. """
    def __init__(self, *args, **kwargs):
        """ Using __init__ method """
        super().__init__(*args, **kwargs)
        self.test_class = Amenity

    def test_name(self):
        """ Check name type """
        test = self.test_class()
        self.assertIsInstance(test.name, str)

if __name__ == "__main__":
    unittest.main()
