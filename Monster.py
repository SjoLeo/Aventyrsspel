import random as rand
import Player
import Worldinfo
import pygame
import Buttons


class Monster():
    def __init__(self):
        self.strength = (rand.randint(8, 15)) * Worldinfo.current_dungeon_floor
        self.hp = (rand.randint(8, 15)) * Worldinfo.current_dungeon_floor

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

class Boss():
    def __init__(self, base_hp, base_strength):
        self.hp = base_hp * Worldinfo.current_dungeon_floor
        self.current_hp = self.hp
        self.damage = base_strength * Worldinfo.current_dungeon_floor

        self.type = rand.choice(['zombie_boss'])
        self.vulnerable_x_coordinate = 0
        self.vulnerable_y_coordinate = 0
        self.boss_hp_percentage = 1

    def draw_health_bar(self, surface, x, y):

        self.boss_hp_percentage = self.current_hp/self.hp

        boss_hp_bar_width = 250
        boss_hp_bar_height = 25

        # outer rectangle
        pygame.draw.rect(surface, (0, 0, 0), (x, y, boss_hp_bar_width, boss_hp_bar_height))
        # inner rectangle
        pygame.draw.rect(surface, (245, 14, 14), (x + 4, y + 4, boss_hp_bar_width - 8, boss_hp_bar_height - 8))

        # health loss
        pygame.draw.rect(surface, (106, 207, 48), (x + 4, y + 4, int((boss_hp_bar_width - 8) * self.boss_hp_percentage), boss_hp_bar_height - 8))

    def generate_vulnerable_spot_coordinates(self, image, x, y, scale):
        width = image.get_width()
        height = image.get_height()
        self.vulnerable_x_coordinate = rand.randint(x, x + width*scale)
        self.vulnerable_y_coordinate = rand.randint(y, y + height*scale)



