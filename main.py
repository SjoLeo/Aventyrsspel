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

def show_text(text, x, y, color):
    test_text = font_alagard.render(text, True, (color))
    screen.blit(test_text, (x, y))

# background
main_menu_background = pygame.image.load("Images/pixil-frame-0.png")
main_menu_background = pygame.transform.scale(main_menu_background, (1200, 675))
active_background = main_menu_background

def background():
    screen.blit(active_background, (0, 0))


# Game Loop

while running:

    screen.fill((60, 50, 217))
    # Graphics
    background()

    # checks if action happened and draws image
    if inventory_button.render_image_button(screen):
        print('clicked')

    if exit_button.render_image_button(screen):
        running = False

    if new_game_button.render_text_button(screen):
        print('clicked')



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()

    
