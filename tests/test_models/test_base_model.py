#!/usr/bin/python3
""" Unittest for BaseModel """
from unittest import TestCase
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime as dt

class BaseModel_Test(unittest.TestCase):
    """ Creating class to test base class. """
    def __init__(self, *args, **kwargs):
        self.test_class = BaseModel
        self.test_name = "BaseModel"

    def test_id(self):
        self.assertIsInstance(self.test_class.id, str)
        self.assertIsInstance(self.test_class.id, UUID)

    def test_create(self):
        base = self.test_class
        now = dt.now()
        self.assertIsInstance(base.test_class.created_at, dt)

    def test_update(self):
        base = self.test_class
        now = dt.now()
        base.dt.now()
        self.assertNotEqual(base.dt, now)

    def test_save(self):
        """ Checking that name is saved """
        test = BaseModel.save('Flavio')
        self.assertEqual(test, {'name': 'Flavio'})

if __name__ == "__main__":
    unittest.main()
