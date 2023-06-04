"""
module: fridge_manager
This module provides a FridgeManager class for managing fridges
"""


class FridgeManager:
    """
    This class managing fridges
    """

    def __init__(self):
        self.fridges = []

    def add_fridge(self, a_fridge):
        """
        This function adds fridges to list
        """
        self.fridges.append(a_fridge)

    def find_fridge_with_capacity(self, capacity):
        """
        This func finds fridges with given capacity in the list
        """
        return [a_fridge for a_fridge in self.fridges if a_fridge.capacity == capacity]

    def find_fridge_with_brand(self, brand):
        """
         This func finds fridges with given brand in the list
        """
        return [a_fridge for a_fridge in self.fridges if a_fridge.brand == brand]

    def print_fridges(self):
        for a_fridge in self.fridges:
            print(a_fridge)
            print("Max usable capacity:", a_fridge.get_max_usable_capacity())

    def __str__(self):
        return "FridgeManager: \n" + "\n".join(str(a_fridge) for a_fridge in self.fridges)
