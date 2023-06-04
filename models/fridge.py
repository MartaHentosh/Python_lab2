"""
module: fridge
This module provides abstract class Fridge
"""
from abc import ABC, abstractmethod


class Fridge(ABC):
    """
    Abstract base class representing a Fridge.
    """
    def __init__(self, brand, model, capacity):
        self.brand = brand
        self.model = model
        self.capacity = capacity

    @abstractmethod
    def get_max_usable_capacity(self):
        """
        Abstract method to be implemented by subclasses.
        This method should return the maximum usable capacity of the fridge.
        """

    def __str__(self):
        return f"Fridge: {self.brand}, {self.model}, {self.capacity}"
