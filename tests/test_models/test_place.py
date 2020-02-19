#!/usr/bin/python3
""" Unittest for Place Class """
from tests.test_models.test_base_model import BaseModel_Test
from models.place import Place


class Place_Test(BaseModel_Test):
    """ Creating class to test Place class. """
    def __init__(self, *args, **kwargs):
        """ Using __init__ method """
        super().__init__(*args, **kwargs)
        self.test_class = Place

    def test_city_id(self):
        """ Check city_id type """
        test = self.test_class()
        self.assertIsInstance(test.city_id, str)

    def test_user_id(self):
        """ Check user_id type """
        test = self.test_class()
        self.assertIsInstance(test.user_id, str)

    def test_name(self):
        """ Check name type """
        test = self.test_class()
        self.assertIsInstance(test.name, str)

    def test_description(self):
        """ Check description type """
        test = self.test_class()
        self.assertIsInstance(test.description, str)

    def test_number_rooms(self):
        """ Check number_rooms type """
        test = self.test_class()
        self.assertIsInstance(test.number_rooms, int)

    def test_number_bathrooms(self):
        """ Check number_bathrooms type """
        test = self.test_class()
        self.assertIsInstance(test.number_bathrooms, int)

    def test_max_guest(self):
        """ Check max_guest type """
        test = self.test_class()
        self.assertIsInstance(test.max_guest, int)

    def test_price_by_night(self):
        """ Check price_by_night type """
        test = self.test_class()
        self.assertIsInstance(test.price_by_night, int)

    def test_latitude(self):
        """ Check latitude type """
        test = self.test_class()
        self.assertIsInstance(test.latitude, float)

    def test_longitude(self):
        """ Check longitude type """
        test = self.test_class()
        self.assertIsInstance(test.longitude, float)

    def test_amenity_ids(self):
        """ Check amenity_ids type """
        test = self.test_class()
        self.assertIsInstance(test.amenity_ids, list)

if __name__ == "__main__":
    unittest.main()
