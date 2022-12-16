import Items
import Monster

class Player():
    def __init__(self, base_strength, base_hp, base_defence, lvl):
        self.strength = base_strength
        self.hp = base_hp
        self.defence = base_defence

        self.damage = base_strength
        self.total_defence = base_defence

        self.lvl = lvl
        self.equipped_weapon = 0
        self.equipped_armour = 0
        self.equipped_potion = 0

        self.weapon_inventory = ['Empty', 'Empty']
        self.armour_inventory = ['Empty', 'Empty']
        self.potion_inventory = ['Empty', 'Empty']

    def add_item_to_inventory(self, item):
        if item.type == 'weapon':
            for _ in self.weapon_inventory:
                self.weapon_inventory[self.equipped_weapon] = item

        if item.type == 'armour':
            for _ in self.armour_inventory:
                self.armour_inventory[self.equipped_armour] = item

        if item.type == 'potion':
            for _ in self.potion_inventory:
                self.potion_inventory[self.equipped_potion] = item

    def add_item_stats(self):
        # adding strength bonus to player
        self.damage = self.strength
        if not self.weapon_inventory[self.equipped_weapon] == 'Empty':
            self.damage = self.weapon_inventory[self.equipped_weapon].strength + self.strength

        # adding defence bonus to player
        self.total_defence = self.defence
        if not self.armour_inventory[self.equipped_armour] == 'Empty':
            self.total_defence = self.armour_inventory[self.equipped_armour].defence + self.defence


    def add_lvl(self, added_lvl):
        self.lvl += added_lvl


player = Player(10, 10, 10, 1)


