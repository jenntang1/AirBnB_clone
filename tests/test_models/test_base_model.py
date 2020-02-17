#!/usr/bin/python3
""" Unittest for BaseModel """
import unittest
from uuid import UUID
from datetime import datetime
from models.base_model import BaseModel


class BaseModel_Test(unittest.TestCase):
    """ Creating class to test base class """

    def __init__(self, *args, **kwargs):
        """ Using __init__ method to initialize BaseModel """
        self.test_class = BaseModel
        self.test_name = "BaseModel"

    def test_id(self):
        """ Check id type """
        self.assertIsInstance(self.test_class.id, str)
        self.assertIsInstance(self.test_class.id, UUID)
        self.assertIsInstance(self.test_name.id, str)
        self.assertIsInstance(self.test_name.id, UUID)

    def test_create(self):
        """ Check created_at type """
        base = self.test_class
        current = datetime.now()
        self.assertIsInstance(base.created_at, datetime)

    def test_update(self):
        """ Check updated_at type """
        base = self.test_class
        current = datetime.now()
        update = base.datetime.now()
        self.assertIsInstance(base.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
