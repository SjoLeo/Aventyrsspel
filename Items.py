import pygame

class Item():
    def __init__(self, strength, hp, defence, icon):
        self.strength = strength
        self.hp = hp
        self.defence = defence
        self.icon = icon

# icons
sword_image = pygame.image.load("Images/Sword.png")

broad_sword_image = pygame.image.load("Images/BroadSword.png")

crossbow_image = pygame.image.load("Images/Cross_bow.png")

chestplate_image = pygame.image.load("Images/Basic_armor.png")

hp_potion_image = pygame.image.load("Images/Health_potion.png")

# weapons

Sword = Item(2, 0, 0, sword_image)
BroadSword = Item(3, 0, 0, broad_sword_image)
"""
Axe = Item(1, 0, 0, main.)
"""
Crossbow = Item(1, 0, 0, crossbow_image)

weapons = [Sword, BroadSword, Crossbow]

# armour

Chestplate = Item(0, 0, 5, chestplate_image)

armours = [Chestplate]

# potion

Potion_of_health = Item(0, 5, 0, hp_potion_image)

potions = [Potion_of_health]

# items

items_list = [weapons, armours, potions]

