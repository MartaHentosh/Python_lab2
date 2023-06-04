"""
module:main
This module serves as the entry point for managing fridges.
It demonstrates the usage of the FridgeManager class and various fridge models such as
FridgeCamera, WineFridge, Freezer, and Minibar.
"""

from manager.fridge_manager import FridgeManager
from models.freezer import Freezer
from models.fridge_camera import FridgeCamera
from models.minibar import Minibar
from models.wine_fridge import WineFridge

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
