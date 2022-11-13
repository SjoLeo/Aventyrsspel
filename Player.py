

class Player():
    def __init__(self, STR, HP, DEF, LVL):
        self.STR = STR
        self.HP = HP
        self.DEF = DEF
        self.LVL = LVL

    def add_stats(self, Added_STR, Added_HP, Added_DEF, ):
        self.STR += Added_STR
        self.HP += Added_HP
        self.DEF += Added_DEF

    def add_LVL(self, Added_LVL):
        self.LVL += Added_LVL


player = Player(10, 10, 10, 1)
