from Main_2 import *

class Item():
    def __init__(self, STR, HP, DEF):
        self.STR = STR
        self.HP = HP
        self.DEF = DEF

    def add_item_to_inventory(self):
        Inventory.append(self)


# weapons
LongSword = Item(2, 0, 0)
BroadSword = Item(3, 0, 0)
Axe = Item(1, 0, 0)

# armour

Chestplate = Item(0, 0, 5)

# potion

Potion_of_health = Item(0, 5, 0)
