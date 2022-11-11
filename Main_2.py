from Items import *
from Monster import *
from Player import *
from main import *

# weapon = 2 slot
weapon = []

# armour = 2 slot
armour = []

# potion = 2 slot
potion = []

# inventory = 6 slots
Inventory = [LongSword, BroadSword, Axe, Chestplate, Potion_of_health]


# Add item stats to player
for item in Inventory:
    player.add_stats(item.STR, item.HP, item.DEF)
