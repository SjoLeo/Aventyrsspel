

class Item():
    def __init__(self, strength, hp, defence):
        self.strength = strength
        self.hp = hp
        self.defence = defence

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


# weapon = 2 slot
weapon = []

# armour = 2 slot
armour = []

# potion = 2 slot
potion = []

# inventory = 6 slots
Inventory = [LongSword, BroadSword, Axe, Chestplate, Potion_of_health]