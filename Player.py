import Items

class Player():
    def __init__(self, base_strength, base_hp, base_defence, lvl):
        self.strength = base_strength
        self.hp = base_hp
        self.defence = base_defence
        self.lvl = lvl

        self.weapon_inventory = [Items.Sword, None]
        self.weapon_1 = self.weapon_inventory[0]
        self.weapon_2 = self.weapon_inventory[1]

        self.armour_inventory = [Items.Chestplate, None]
        self.armour_1 = self.armour_inventory[0]
        self.armour_2 = self.armour_inventory[1]

    def add_item_to_inventory(self, item):
        if item.type == 'weapon':
            self.weapon_inventory.append(item)
    def add_lvl(self, added_lvl):
        self.lvl += added_lvl


player = Player(10, 10, 10, 1)

print(player.weapon_inventory)

player.add_item_to_inventory(Items.Sword)

print(player.weapon_inventory)

