

class Player():
    def __init__(self, strength, hp, defence, lvl):
        self.strength = strength
        self.hp = hp
        self.defence = defence
        self.lvl = lvl

    def add_stats(self, added_strength, added_hp, added_defence):
        self.strength += added_strength
        self.hp += added_hp
        self.defence += added_defence

    def add_lvl(self, added_lvl):
        self.lvl += added_lvl


player = Player(10, 10, 10, 1)
