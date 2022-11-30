import Buttons
import Items
import Monster
import TextButtons
import Player
import LootChest
import random
import pygame
import Door
import time
import GameState

pygame.init()

# Screen
width = 1200
height = 675
screen = pygame.display.set_mode((width, height))


pygame.display.set_caption("Test Caption")


clock = pygame.time.Clock()

random.seed(69)
game_state = GameState.GameState()
running = True

# Game Loop
while running:
    # pos = pygame.mouse.get_pos()
    # print(pos)
    clock.tick(60)

    game_state.state_manager()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
