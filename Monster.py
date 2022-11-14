import random as rand



class Monster():
    def __init__(self, STR, HP):
        self.STR = STR
        self.HP = HP


    def typ(self):

        monster = rand.randint(1, 10)

        if monster in range(1, 5):
            return "zombie"

        else:
            return "spindel"

# def STR(self):


# def HP(self):

Monster = Monster(3, 5)
print(Monster.typ())

