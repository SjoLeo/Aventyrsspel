import pygame
import Player
import copy

class Item():
    def __init__(self, strength, hp, defence, icon, type, name):
        self.name = name
        self.strength = strength
        self.hp = hp
        self.defence = defence
        self.icon = icon
        self.type = type

    def __deepcopy__(self, memo): # memo is a dict of id's to copies
        id_self = id(self)        # memoization avoids unnecesary recursion
        _copy = memo.get(id_self)
        if _copy is None:
            _copy = type(self)(
                copy.deepcopy(self.strength, memo),
                copy.deepcopy(self.hp, memo),
                copy.deepcopy(self.defence, memo),
                copy.copy(self.icon),
                copy.deepcopy(self.type, memo),
                copy.deepcopy(self.name, memo))
            memo[id_self] = _copy
        return _copy



# icons
sword_image = pygame.image.load("Images/Sword.png")
broad_sword_image = pygame.image.load("Images/BroadSword.png")
crossbow_image = pygame.image.load("Images/Cross_bow.png")

chestplate_image = pygame.image.load("Images/Basic_armor.png")

hp_potion_image = pygame.image.load("Images/Health_potion.png")

# stats change in gamestate loot chest
# weapons
Sword = Item(0, 0, 0, sword_image, 'weapon', 'Sword')
BroadSword = Item(0, 0, 0, broad_sword_image, 'weapon', 'Broadsword')
Crossbow = Item(0, 0, 0, crossbow_image, 'weapon', 'Crossbow')

weapons = [Sword, BroadSword, Crossbow]

# armour
Chestplate = Item(0, 0, 0, chestplate_image, 'armour', 'Chestplate')

armours = [Chestplate]

# potion
Potion_of_health = Item(0, 0, 0, hp_potion_image, 'potion', 'Potion_of_health')

potions = [Potion_of_health]

# items
items_list = [weapons, armours, potions]

