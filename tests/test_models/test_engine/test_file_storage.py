#!/usr/bin/python3
""" Unittest for file storage """
import os
import unittest
from models.engine.file_storage import FileStorage
from tests.test_models.test_base_model import BaseModel_Test


class FileStorage_Test(unittest.TestCase):
    """ Creating class to test File Storage """
    def __init__(self, *args, **kwargs):
        """ Using __init__ method """
        super().__init__(*args, **kwargs)
        self.test_class = FileStorage

    def test_file_path(self):
        """ Check file_path type """
        test = self.test_class()
        self.assertIsInstance(test.__file_path, str)

    def tearDown(self):
        """ Using tearDown method """
        try:
            os.remove("file.json")
        except:
            pass

    def test_objects(self):
        """ Check __objects type """
        test = self.test_class()
        self.assertIsInstance(test.__objects, dict)

    def tearDown(self):
        """ Using tearDown method """
        try:
            os.remove("file.json")
        except:
            pass

    def test_empty(self):
        """ Check empty file """
        test = self.test_class()
        self.assertTrue(os.stat(test.__file_path).st_size == 0)

    def tearDown(self):
        """ Using tearDown method """
        try:
            os.remove("file.json")
        except:
            pass
