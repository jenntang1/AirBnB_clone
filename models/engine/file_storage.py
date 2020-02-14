#!/usr/bin/python3
""" FileStorage Implementation """
import json


class FileStorage:
    """ Creating a class to serialize instances to a JSON file
    and deserialize JSON file to instances.
    Attributes:
        -------------- private class attributes --------------
        __file_path: path to the JSON file that's a string
        __objects: store all objects by <class name>.id that's
                   an empty dictionary
    """
    __file_path
    __objects

    def all(self):
        """ Creating public instance method that returns
        the dictionary __objects.
        """
        return self.__dict__.__objects

    def new(self, obj):
        """ Creating public instance method that sets in
        __objects the obj with key <obj class name>.id.
        """
        self.__objects[obj.id] = obj

    def save(self):
        """ Creating public instance method that serializes
        __objects to the JSON file, __file_path.
        """
        with open(__file_path, 'w') as save_json:
            save_json.write(json.dumps(__objects))

    def reload(self):
        """ Creating public instance method that deserializes
        the JSON file to __objects.
        """
        if __file_path is not None:
            json.loads(__file_path)
