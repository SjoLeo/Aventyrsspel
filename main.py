


import pygame


# initierar pygame
pygame.init()

# Creates the screen
screen = pygame.display.set_mode((1280, 645))

running = True

# Title and Window
pygame.display.set_caption("Test Caption")
# icon = pygame.image.load("")
# pygame.display.set_icon(icon)



# Game Loop

while running:

    screen.fill((60, 50, 217))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

    'hello'
