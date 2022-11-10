from Items import *
from Monster import *
from Player import *

Inventory = [LongSword, BroadSword, Axe, Chestplate, Potion_of_health]

print(player.STR, player.HP, player.DEF)

# Lägga till item stats på spelare
for item in Inventory:
    player.add_stats(item.STR, item.HP, item.DEF)

print(player.STR, player.HP, player.DEF)
