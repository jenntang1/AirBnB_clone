#!/usr/bin/python3
""" Unittest for BaseModel """
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel


class BaseModel_Test(unittest.TestCase):
    """ Creating class to test base class """
    def __init__(self, *args, **kwargs):
        """ Using __init__ method to initialize BaseModel """
        super().__init__(*args, **kwargs)
        self.test_class = BaseModel
        self.test_name = "BaseModel"

    def test_id(self):
        """ Check id type """
        test = self.test_class()
        self.assertIsInstance(test.id, str)

    def test_create(self):
        """ Check created_at type """
        test = self.test_class()
        self.assertIsInstance(test.created_at, datetime)

    def test_update(self):
        """ Check updated_at type """
        test = self.test_class()
        self.assertIsInstance(test.updated_at, datetime)

    def tearDown(self):
        """ Using tearDown method """
        try:
            os.remove("file.json")
        except:
            pass
