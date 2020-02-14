#!/usr/bin/python3
""" FileStorage Implementation """
import json
import os


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
    __objects

    def all(self):
        """ Creating public instance method that returns
        the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """ Creating public instance method that sets in
        __objects the obj with key <obj class name>.id.
        """
        self.__objects[obj.id] = obj

    def save(self):
        """ Creating public instance method that serializes
        __objects to the JSON file, __file_path.
        """
        temp_dict = dict(self.__objects)
        for key, value in temp_dict.items():
            with open(self.__file_path, 'w') as save_json:
                json.dump(temp_dict, save_json)

    def reload(self):
        """ Creating public instance method that deserializes
        the JSON file to __objects.
        """
        if self.__file_path is not None:
            json.load(self.__file_path)
