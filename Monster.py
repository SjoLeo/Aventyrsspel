import random as rand



class Monster():
    def __init__(self, typ, STR, HP):
        self.STR = STR
        self.HP = HP
        self.typ = typ


    def typ(self):

        monster = rand.randint(1, 10)

        if monster in range(1, 5):
            typ = "zombie"

        else:
            typ = "spindel"

# def STR(self):


# def HP(self):

Zombie = Monster("zombie", 3, 5)
