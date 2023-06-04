"""
This module provides Fridge Camera class
"""
from decorator import logged
from invalid_brand_exception import InvalidBrandException
from models.fridge import Fridge


class FridgeCamera(Fridge):
    """
    Class represents fridge camera
    """
    VOLUME_PER_KILOGRAM = 0.01

    def __init__(self, brand, model, capacity, entries, belt_type, belt_speed, max_sausage_weight):
        super().__init__(brand, model, capacity)
        self.entries = entries
        self.belt_type = belt_type
        self.belt_speed = belt_speed
        self.max_sausage_weight = max_sausage_weight

    def get_max_usable_capacity(self):
        return self.max_sausage_weight / self.VOLUME_PER_KILOGRAM

    @logged(InvalidBrandException, "file")
    def check_brand(self):
        """
        This method checks if the brand of the fridge is valid.
        """
        if self.brand == "InvalidBrand":
            raise InvalidBrandException(self.brand)

    def __str__(self):
        return f"FridgeCamera: {self.brand}, {self.model}, {self.capacity}, {self.entries}, " \
               f"{self.belt_type}, {self.belt_speed}, {self.max_sausage_weight}"
