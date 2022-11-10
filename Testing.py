from Main import *

Inventory = [LongSword, BroadSword, Axe, Chestplate, Potion_of_health]

STR_Player = 0
HP_Player = 0
DEF_Player = 0
for item in Inventory:
    STR_Player += item.STR
    HP_Player += item.HP
    DEF_Player += item.DEF