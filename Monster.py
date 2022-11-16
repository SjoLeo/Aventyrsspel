import random as rand
import Player


class Monster():
    def __init__(self):
        self.strength = Player.player.lvl*10*(rand.randint(9, 12)/10)
        '''self.hp = hp'''


    def typ(self):

        monster = rand.randint(1, 10)

        if monster in range(1, 5):
            return "zombie"

        else:
            return "spindel"

# def STR(self):


# def HP(self):

Monster = Monster()
print(Monster.typ())
print(Monster.strength)

