import Items

class Player():
    def __init__(self, base_strength, base_hp, base_defence, lvl):
        self.strength = base_strength
        self.hp = base_hp
        self.defence = base_defence
        self.lvl = lvl

        self.weapon_inventory = [Items.BroadSword, 'Empty']
        self.armour_inventory = [Items.Chestplate, 'Empty']


    def add_item_to_inventory(self, item, swap_with):
        if item.type == 'weapon':
            empty = False
            for index, weapon in enumerate(self.weapon_inventory):
                if weapon == 'Empty':
                    self.weapon_inventory[index] = item
                    empty = True

            if empty == False:
                for index, weapon in enumerate(self.weapon_inventory):
                    if weapon == item:
                        self.weapon_inventory[index] = swap_with







    def add_lvl(self, added_lvl):
        self.lvl += added_lvl


player = Player(10, 10, 10, 1)


