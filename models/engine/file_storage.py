#!/usr/bin/python3
""" FileStorage Implementation """
import json
from os import path


class FileStorage:
    """ Creating a class to serialize instances to a JSON file
    and deserialize JSON file to instances.
    Attributes:
        -------------- private class attributes --------------
        __file_path: path to the JSON file that's a string
        __objects: store all objects by <class name>.id that's
                   an empty dictionary
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Creating public instance method that returns
        the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Creating public instance method that sets in
        __objects the obj with key <obj class name>.id.
        """
        key = str(type(obj).__name__) + "." + str(obj)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Creating public instance method that serializes
        __objects to the JSON file, __file_path.
        """
        temp_dict = dict(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w') as save_json:
            instance = json.dump(temp_dict, save_json)
            for key, value in instance.to_dict():
                temp_dict[key] = value.to_dict()

    def reload(self):
        """ Creating public instance method that deserializes
        the JSON file to __objects.
        """
        if path.exists(FileStorage.__file_path):
            from models.base_model import BaseModel
            instance = {}
            with open(FileStorage.__file_path, 'r') as from_json:
                instance = json.load(from_json)
                for key, value in instance.items():
                    FileStorage.__objects = BaseModel(**value)
