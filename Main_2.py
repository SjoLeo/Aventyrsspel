import Items

import Player


# Add item stats to player
for item in Items.Inventory:
    Player.player.add_stats(item.strength, item.hp, item.defence)
print(Player.player.strength, Player.player.hp, Player.player.defence)
# Add items to inventory
print(len(Items.Inventory))
Items.LongSword.add_item_to_inventory()
print(len(Items.Inventory))



