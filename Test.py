import random
class Item():
    def __init__(self):
        self.strength = 0

sword1 = Item()
sword2 = Item()
inventory = []
sword1.strength = 1
inventory.append(sword1)
sword2.strength = 2
inventory.append(sword2)
print(inventory)
print(inventory[0].strength)
print(inventory[1].strength)