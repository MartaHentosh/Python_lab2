"""
module:freezer
This module provides Freezer class
"""
from models.fridge import Fridge


class Freezer(Fridge):
    """
    Class represents freezer
    """

    def __init__(self, brand, model, capacity, max_ice_weight, max_ice_volume):
        super().__init__(brand, model, capacity)
        self.max_ice_weight = max_ice_weight
        self.max_ice_volume = max_ice_volume

    def get_max_usable_capacity(self):
        """
        Calculates and returns the maximum usable capacity of the object.
        """
        return self.max_ice_weight * self.max_ice_volume

    def __str__(self):
        return f"Freezer: {self.brand}, {self.model}, {self.capacity}," \
               f"{self.max_ice_weight}, {self.max_ice_volume}"
