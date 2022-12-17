import random as rand
import Player




class Monster():
    def __init__(self):
        self.strength = Player.player.lvl*(rand.randint(9, 12))
        self.hp = Player.player.lvl*(rand.randint(9, 12))

        monsters = ['spider', 'zombie']
        self.type = rand.choice(monsters)

    def monster_position(self):
        if self.type == 'spider':
            x_coordinate = rand.randint(100, 300)
            y_coordinate = rand.randint(100, 300)
            coordinates = [x_coordinate, y_coordinate]
            return coordinates

        if self.type == 'zombie':
            x_coordinate = rand.randint(100, 400)
            y_coordinate = rand.randint(170, 190)
            coordinates = [x_coordinate, y_coordinate]
            return coordinates
