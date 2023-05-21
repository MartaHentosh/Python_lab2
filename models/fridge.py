class Fridge:
    def __init__(self, brand, model, capacity):
        self.brand = brand
        self.model = model
        self.capacity = capacity

    def get_max_usable_capacity(self):
        pass

    def __str__(self):
        return f"Fridge: {self.brand}, {self.model}, {self.capacity}"
