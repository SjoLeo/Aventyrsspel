import time

import pygame
import GameState
import random

pygame.display.set_caption("Test Caption")

# Screen
width = 1200
height = 675
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

#random.seed(10)
game_state = GameState.GameState()
running = True

# Game Loop
prev_time = time.time()
dt = 0
while running:
    #print(pygame.mouse.get_pos())
    clock.tick(30)
    #print(clock)

    game_state.state_manager(dt)

    now = time.time()
    dt = now - prev_time
    prev_time = now
