#!/usr/bin/python3
""" Place Class Implementation / Importing BaseModel """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Subclass that inherits from BaseModel
    Attributes:
        ----------- public class attributes -----------
        city_id: empty string but will be City.id
        user_id: empty string but will be User.id
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
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
