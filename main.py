import Buttons
import TextButton


import pygame



# initiates pygame
pygame.init()

# Creates the screen
width = 1200
height = 675
screen = pygame.display.set_mode((width, height))

running = True

# Title and Window
pygame.display.set_caption("Test Caption")
# icon = pygame.image.load("")
# pygame.display.set_icon(icon)
inventory_image = pygame.image.load('Images/Inventory_slot.png').convert_alpha()
exit_image = pygame.image.load('Images/exit.png').convert_alpha()

# making button objects
inventory_button = Buttons.Button(inventory_image, 0, 0, 0.3)
exit_button = Buttons.Button(exit_image, width-150, 0, 0.5)

new_game_button = TextButton.TextButton(200, 200, 'New Game', 'blue')

# Text
font_alagard = pygame.font.Font("Fonts/alagard.ttf", 100)

textX = 200
textY = 200

def show_test_text(x, y):
    test_text = font_alagard.render("Test Text", True, (225, 225, 225))
    screen.blit(test_text, (x, y))

# Game Loop

while running:

    screen.fill((60, 50, 217))
    # checks if action happened and draws image
    if inventory_button.draw_button(screen):
        print('clicked')

    if exit_button.draw_button(screen):
        running = False

    if new_game_button.draw_text(screen):
        print('clicked')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    show_test_text(textX, textY)
    pygame.display.update()

    
