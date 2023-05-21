from models.fridge import Fridge


class Minibar(Fridge):
    def __init__(self, brand, model, capacity, max_drinks_weight, max_drinks_volume):
        super().__init__(brand, model, capacity)
        self.max_drinks_weight = max_drinks_weight
        self.max_drinks_volume = max_drinks_volume

    def get_max_usable_capacity(self):
        return self.max_drinks_weight * self.max_drinks_volume

    def __str__(self):
        return f"Minibar: {self.brand}, {self.model}, {self.capacity}," \
               f"{self.max_drinks_weight}, {self.max_drinks_volume}"
