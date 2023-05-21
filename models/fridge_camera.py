from models.fridge import Fridge


class FridgeCamera(Fridge):
    VOLUME_PER_KILOGRAM = 0.01

    def __init__(self, brand, model, capacity, entries, belt_type, belt_speed, max_sausage_weight):
        super().__init__(brand, model, capacity)
        self.entries = entries
        self.belt_type = belt_type
        self.belt_speed = belt_speed
        self.max_sausage_weight = max_sausage_weight

    def get_max_usable_capacity(self):
        return self.max_sausage_weight / self.VOLUME_PER_KILOGRAM

    def __str__(self):
        return f"FridgeCamera: {self.brand}, {self.model}, {self.capacity}, {self.entries}, " \
               f"{self.belt_type}, {self.belt_speed}, {self.max_sausage_weight}"
