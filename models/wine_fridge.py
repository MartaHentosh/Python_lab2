"""
module:wine_fridge
This module provides Wine Fridge class
"""
from models.fridge import Fridge


class WineFridge(Fridge):
    """
    Class represents wine fridge
    """
    def __init__(self, brand, model, capacity, max_bottles_weight, max_bottles_volume):
        super().__init__(brand, model, capacity)
        self.max_bottles_weight = max_bottles_weight
        self.max_bottles_volume = max_bottles_volume

    def get_max_usable_capacity(self):
        """
         Calculates and returns the maximum usable capacity of the object.
        """
        return self.max_bottles_weight * self.max_bottles_volume

    def __str__(self):
        return f"WineFridge: {self.brand}, {self.model}, {self.capacity}," \
               f"{self.max_bottles_weight}, {self.max_bottles_volume}"
