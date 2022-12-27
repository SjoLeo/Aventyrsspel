import random as rand
import Player
import Worldinfo
import pygame




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

class Boss():
    def __init__(self, base_hp, base_strength):
        self.hp = base_hp * Worldinfo.current_dungeon_floor
        self.current_hp = self.hp
        self.damage = base_strength * Worldinfo.current_dungeon_floor
        self.current_health_bar_image = health_bar_100

        self.type = rand.choice(['zombie_boss'])


    def calculate_health_bar_image(self):
        percentage = self.current_hp/self.hp
        # checks which health bar is nearest to the current health
        if 0.94 <= percentage <= 1:
            self.current_health_bar_image = health_bar_100
        elif 0.82 <= percentage < 94:
            self.current_health_bar_image = health_bar_88
        elif 0.69 <= percentage < 0.82:
            self.current_health_bar_image = health_bar_75
        elif 0.57 <= percentage < 0.69:
            self.current_health_bar_image = health_bar_63
        elif 0.44 <= percentage < 0.57:
            self.current_health_bar_image = health_bar_50
        elif 0.32 <= percentage < 0.44:
            self.current_health_bar_image = health_bar_38
        elif 0.19 <= percentage < 0.32:
            self.current_health_bar_image = health_bar_25
        elif 0 < percentage < 0.19:
            self.current_health_bar_image = health_bar_13
        else:
            self.current_health_bar_image = health_bar_0

        return self.current_health_bar_image


# health bar images
health_bar_100 = pygame.image.load('Images/health_bars/health_bar_100%.png')
health_bar_88 = pygame.image.load('Images/health_bars/health_bar_88%.png')
health_bar_75 = pygame.image.load('Images/health_bars/health_bar_75%.png')
health_bar_63 = pygame.image.load('Images/health_bars/health_bar_63%.png')
health_bar_50 = pygame.image.load('Images/health_bars/health_bar_50%.png')
health_bar_38 = pygame.image.load('Images/health_bars/health_bar_38%.png')
health_bar_25 = pygame.image.load('Images/health_bars/health_bar_25%.png')
health_bar_13 = pygame.image.load('Images/health_bars/health_bar_13%.png')
health_bar_0 = pygame.image.load('Images/health_bars/health_bar_0%.png')
