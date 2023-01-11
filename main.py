import time

import pygame
import GameState
import random

pygame.display.set_caption("Test Caption")


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

