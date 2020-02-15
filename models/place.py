#!/usr/bin/python3
""" Place Class Implementation / Importing BaseModel """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Subclass that inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        """ Implementing __init__ method as the constructor.
        Args:
            args: positional command line args
            kwargs: keyword command line args
        Attributes:
            ----------- public class attributes -----------
            city_id: empty string but will be City.id
            user_id: empty strinb but will be User.id
            name: empty string
            description: empty string
            number_rooms: integer 0
            number_bathrooms: integer 0
            max_guest: integer 0
            price_by_night: integer 0
            latitude: float 0.0
            longitude: float 0.0
            amenity_ids: empty list of string but will be
                         Amenity.id
        """
        super(Place, self).__init__(*args, **kwargs)
        self.city_id = kwargs.get("city_id")
        self.user_id = kwargs.get("user_id")
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = kwargs.get("amenity_ids")
