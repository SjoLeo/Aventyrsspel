import time
import pygame
import GameState

'''
info about pygame and our game state:
all scenes lies within a loop, one cycle of the loop is one frame and all 
of the images are redrawn every frame. We have the game state to keep track of 
what scenes should be drawn and at what time. 
'''

pygame.display.set_caption("Test Caption")
clock = pygame.time.Clock()

game_state = GameState.GameState()
running = True

# Game Loop
prev_time = time.time()
dt = 0
while running:
    clock.tick(30)
    # all scenes are run here
    game_state.state_manager(dt)

    # delta time makes animations consistent
    # does not matter what frame rate you have
    now = time.time()
    dt = now - prev_time
    prev_time = now
