

class Item():
    def __init__(self, strength, hp, defence):
        self.strength = strength
        self.hp = hp
        self.defence = defence






# weapons

LongSword = Item(2, 0, 0)
BroadSword = Item(3, 0, 0)
Axe = Item(1, 0, 0)

weapons = [LongSword, BroadSword, Axe]

# armour

Chestplate = Item(0, 0, 5)

armours = [Chestplate]

# potion

Potion_of_health = Item(0, 5, 0)

potions = [Potion_of_health]

# items

items_list = [weapons, armours, potions]