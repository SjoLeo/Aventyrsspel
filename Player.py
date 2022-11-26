import Items

class Player():
    def __init__(self, base_strength, base_hp, base_defence, lvl):
        self.strength = base_strength
        self.hp = base_hp
        self.defence = base_defence
        self.lvl = lvl
        self.inventory = [Items.Sword, Items.BroadSword, Items.Crossbow, Items.Chestplate]
        self.selected_inventory = [Items.Chestplate, Items.Sword, Items.Crossbow]
        self.weapon_1 = Items.Sword
        self.weapon_2 = Items.Crossbow
    def add_item_to_inventory(self, item):
        self.inventory.append(item)

    def add_inventory_stats(self):
        for item in self.selected_inventory:
            self.strength += item.strength
            self.hp += item.hp
            self.defence += item.defence

    def add_lvl(self, added_lvl):
        self.lvl += added_lvl


player = Player(10, 10, 10, 1)

player.add_inventory_stats()
print(player.strength, player.hp, player.defence)
