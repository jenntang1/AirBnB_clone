#!/usr/bin/python3
""" Unittest for BaseModel """
from unittest import TestCase
from models.base_model import BaseModel


class BaseModel_Test(unittest.TestCase):
    """ Creating class to test base class. """

    def test_save(self):
        """ Checking that name is saved """
        test = BaseModel.save('Flavio')
        self.assertEqual(test, {'name': 'Flavio'})

    def test_type(self):
        """ Checking type """
        test = BaseModel.to_dict()
        self.assertIs(type(test), str)

if __name__ == "__main__":
    unittest.main()
