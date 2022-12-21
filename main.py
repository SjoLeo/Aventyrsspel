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
while running:
    #print(pygame.mouse.get_pos())
    clock.tick(60)

    game_state.state_manager()

