#!/usr/bin/python3
""" Unittest for file storage """
import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage


class FileStorage_Test(unittest.TestCase):
    """ Creating class to test File Storage """
    def __init__(self, *args, **kwargs):
        """ Using __init__ method """
        super().__init__(*args, **kwargs)
        self.test_class = FileStorage

    def test_file_path(self):
        """ Check file_path type """
        test = self.test_class()
        self.assertIsInstance(test._FileStorage__file_path, str)

    def tearDown(self):
        """ Using tearDown method """
        try:
            os.remove("file.json")
        except:
            pass

    def test_objects(self):
        """ Check __objects type """
        test = self.test_class()
        self.assertIsInstance(test._FileStorage__objects, dict)

    def tearDown(self):
        """ Using tearDown method """
        try:
            os.remove("file.json")
        except:
            pass

    def test_empty(self):
        """ Check empty file """
        storage.save()
        test = self.test_class()
        self.assertFalse(os.stat(test._FileStorage__file_path).st_size == 0)

    def tearDown(self):
        """ Using tearDown method """
        try:
            os.remove("file.json")
        except:
            pass

    def test_file_exist(self):
        """ Check file.json exists file """
        self.assertFalse(os.path.exists("file.json"))

    def tearDown(self):
        """ Using tearDown method """
        try:
            os.remove("file.json")
        except:
            pass
