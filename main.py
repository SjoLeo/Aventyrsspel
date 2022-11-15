import Buttons



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
inventory_image = pygame.image.load('Images/Inventory_slot.png').convert_alpha()
exit_image = pygame.image.load('Images/exit.png').convert_alpha()

inventory_button = Buttons.Button(inventory_image, 0, 0, 0.3)
exit_button = Buttons.Button(exit_image, 1100, 0, 0.05)
# Game Loop

while running:

    screen.fill((60, 50, 217))
    # checks if action happened and draws image
    if inventory_button.draw_button(screen):
        print('clicked')

    if exit_button.draw_button(screen):
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

    
