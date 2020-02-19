#!/usr/bin/python3
""" Unittest for State Class """
from tests.test_models.test_base_model import BaseModel_Test
from models.state import State


class State_Test(BaseModel_Test):
    """ Creating class to test State class """
    def __init__(self, *args, **kwargs):
        """ Using __init__ method """
        super().__init__(*args, **kwargs)
        self.test_class = State

    def test_state(self):
        """ Check name type """
        test = self.test_class()
        self.assertIsInstance(test.name, str)
