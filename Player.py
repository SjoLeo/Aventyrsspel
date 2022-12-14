import Items

class Player():
    def __init__(self, base_strength, base_hp, base_defence, lvl):
        self.strength = base_strength
        self.hp = base_hp
        self.defence = base_defence
        self.lvl = lvl
        self.equipped_weapon = 0
        self.equipped_armour = 0
        self.equipped_potion = 0

        self.armour_inventory = ['Empty', 'Empty']
        self.potion_inventory = ['Empty', 'Empty']

    def add_item_to_inventory(self, item):
        if item.type == 'weapon':
            for _ in self.weapon_inventory:
                self.weapon_inventory[self.equipped_weapon] = item

        if item.type == 'armour':
            for _ in self.armour_inventory:
                self.armour_inventory[self.equipped_armour] = item









    def add_lvl(self, added_lvl):
        self.lvl += added_lvl


player = Player(10, 10, 10, 1)


