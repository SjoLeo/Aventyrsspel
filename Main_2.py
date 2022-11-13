import Items

import Player

# Add item stats to player
for item in Items.Inventory:
    Player.player.add_stats(item.STR, item.HP, item.DEF)
print(Player.player.STR, Player.player.HP, Player.player.DEF)
# Add items to inventory
print(len(Items.Inventory))
Items.LongSword.add_item_to_inventory()
print(len(Items.Inventory))
