from models.fridge_camera import FridgeCamera
from models.freezer import Freezer
from models.wine_fridge import WineFridge
from models.minibar import Minibar


class FridgeManager:
    def __init__(self):
        self.fridges = []

    def add_fridge(self, a_fridge):
        self.fridges.append(a_fridge)

    def find_fridge_with_capacity(self, capacity):
        return [a_fridge for a_fridge in self.fridges if a_fridge.capacity == capacity]

    def find_fridge_with_brand(self, brand):
        return [a_fridge for a_fridge in self.fridges if a_fridge.brand == brand]

    def print_fridges(self):
        for a_fridge in self.fridges:
            print(a_fridge)
            print("Max usable capacity:", a_fridge.get_max_usable_capacity())

    def __str__(self):
        return "FridgeManager: \n" + "\n".join(str(a_fridge) for a_fridge in self.fridges)


if __name__ == "__main__":
    fridgeManager = FridgeManager()
    fridgeManager.add_fridge(FridgeCamera("LG", "GW-B509MUM", 384, 2, "electric", 2.5, 500))
    fridgeManager.add_fridge(FridgeCamera("Samsung", "MSK", 300, 2, "electrical", 3, 400))
    fridgeManager.add_fridge(WineFridge("Whirlpool", "FWC 455", 70, 36, 50))
    fridgeManager.add_fridge(WineFridge("Klarstein", "ABC123", 60, 26, 40))
    fridgeManager.add_fridge(Freezer("Prime Technics", "MRF-8050W", 145, 120, 120))
    fridgeManager.add_fridge(Freezer("Vivax", "CFR-142", 146, 120, 120))
    fridgeManager.add_fridge(Minibar("MYSTERY", "CS 15141 M", 46, 40, 40))
    fridgeManager.add_fridge(Minibar("Philco", "PW8F", 21, 15, 15))

    fridgeManager.print_fridges()

    capacityFridges = fridgeManager.find_fridge_with_capacity(60)
    print("Fridges with capacity 60:")
    for fridge in capacityFridges:
        print(fridge)

    brandFridges = fridgeManager.find_fridge_with_brand("Samsung")
    print("Fridges with brand Samsung:")
    for fridge in brandFridges:
        print(fridge)
