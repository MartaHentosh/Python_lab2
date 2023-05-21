from models.fridge import Fridge


class Freezer(Fridge):
    def __init__(self, brand, model, capacity, max_ice_weight, max_ice_volume):
        super().__init__(brand, model, capacity)
        self.max_ice_weight = max_ice_weight
        self.max_ice_volume = max_ice_volume

    def get_max_usable_capacity(self):
        return self.max_ice_weight * self.max_ice_volume

    def __str__(self):
        return f"Freezer: {self.brand}, {self.model}, {self.capacity}," \
               f"{self.max_ice_weight}, {self.max_ice_volume}"
