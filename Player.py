import Items
import Monster


class Player():
    def __init__(self, base_strength, base_hp, base_defence, lvl):
        self.current_combo = 1

        self.strength = base_strength
        self.hp = base_hp
        self.defence = base_defence

        self.damage = base_strength * self.current_combo
        self.total_defence = base_defence
        self.current_hp = base_hp

        self.exp = 0
        # exp needed to level up
        self.level_up_exp = 100

        self.lvl = lvl
        self.equipped_weapon = 0
        self.equipped_armour = 0
        self.equipped_potion = 0

        self.weapon_inventory = ['Empty', 'Empty']
        self.armour_inventory = ['Empty', 'Empty']
        self.potion_inventory = ['Empty', 'Empty']





    def add_item_to_inventory(self, item):
        if item.type == 'weapon':
            self.weapon_inventory[self.equipped_weapon] = item

        if item.type == 'armour':
            self.armour_inventory[self.equipped_armour] = item

        if item.type == 'potion':
            self.potion_inventory[self.equipped_potion] = item

    def update_player_stats(self):
        # adding strength bonus to player
        self.damage = self.strength * self.current_combo
        if not self.weapon_inventory[self.equipped_weapon] == 'Empty':
            self.damage = (self.weapon_inventory[self.equipped_weapon].strength + self.strength) * self.current_combo

        # adding defence bonus to player
        self.total_defence = self.defence
        if not self.armour_inventory[self.equipped_armour] == 'Empty':
            self.total_defence = self.armour_inventory[self.equipped_armour].defence + self.defence

    def calculate_exp_overflow(self):
        if self.exp >= self.level_up_exp:
            self.exp = self.exp - self.level_up_exp
            self.lvl += 1
            self.strength += 5
            self.defence += 2
            self.update_player_stats()
            self.level_up_exp += 30


    def drink_potion(self):
        if not self.potion_inventory[self.equipped_potion] == 'Empty':
            # check potion type
            if self.potion_inventory[self.equipped_potion].name == 'Potion_of_health':
                if self.current_hp + 3 <= self.hp:
                    self.current_hp += 3
                    self.potion_inventory[self.equipped_potion] = 'Empty'
                else:
                    self.current_hp = self.hp
                    self.potion_inventory[self.equipped_potion] = 'Empty'


player = Player(10, 10, 2, 1)


