#!/usr/bin/python3
""" Unit tests for file storage """
from unittest import TestCase
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from test.testmodels.test_base_model import TestBaseModel


class FileStorage_Test(unittest.TestCase):
    """ Creating class to test File Storage """
    def __init__(self, *args, **kwargs):
        """ Using __init__ method to initialize FileStorage """
        super().__init__(*args, **kwargs)
        self.test_class = FileStorage
        self.test_name = "FileStorage"

    def test_file_path(self):
        """ Check file_path type """
        test = self.test_file_path()
        self.assertIsInstance(test.id, file)
        pass

    def test_objects(self):
        """ Check created_at type """
        test = self.test_objects()
        self.assertIsInstance(test.__objects, dict)
        pass

if __name__ == "__main__":
    unittest.main()
