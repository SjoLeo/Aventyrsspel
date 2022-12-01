import random as rand
import Player


class Monster():
    def __init__(self):
        self.strength = Player.player.lvl*(rand.randint(9, 12))
        self.hp = Player.player.lvl*(rand.randint(9, 12))

    def monster_type(self):

        monster = rand.randint(1, 10)

        if monster in range(1, 5):
            return "zombie"

        else:
            return "spindel"


'''
print(monster.type())
print(f'styrka:{monster.strength} hp: {monster.hp} ')'''

