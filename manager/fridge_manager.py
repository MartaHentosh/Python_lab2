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

    def __len__(self):
        """
        Returns the length of the fridge manager
        """
        return len(self.fridges)

    def __getitem__(self, index):
        """
        Returns the fridge at the given index
        """
        return self.fridges[index]

    def __iter__(self):
        """
        Returns an iterator for iterating over the fridges
        """
        return iter(self.fridges)

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

    def execute_abstract_method(self):
        """
        Returns a list of results from executing the do_something() method on each fridge object
        """
        return [fridge.do_something() for fridge in self.fridges]

    def enumerate_fridges(self):
        """
        Returns a concatenation of the object and its index for each fridge object
        """
        return [(index, fridge) for index, fridge in enumerate(self.fridges)]

    def zip_results(self):
        """
        Returns a concatenation of the object and the result of executing the method from
        point 1 for each fridge object
        """
        results = self.execute_abstract_method()
        return list(zip(self.fridges, results))

    def get_attributes_by_type(self, data_type):
        """
        Returns a dictionary with attributes and their values of
        a specific data type for each fridge object
        """
        return {fridge: {attr: value for attr, value in fridge.__dict__.items() if isinstance(value, data_type)}
                for fridge in self.fridges}

    def check_condition(self, condition):
        """
        Checks if all objects in the fridge manager satisfy a certain condition
        """
        all_objects = all(condition(fridge) for fridge in self.fridges)
        any_object = any(condition(fridge) for fridge in self.fridges)
        return {"all": all_objects, "any": any_object}

    def __str__(self):
        return "FridgeManager: \n" + "\n".join(str(a_fridge) for a_fridge in self.fridges)
