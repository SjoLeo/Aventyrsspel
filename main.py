import Buttons
import TextButtons


import pygame

import Door

import time

# functions

def show_text(text, x, y, color):
    test_text = font_alagard.render(text, True, (color))
    screen.blit(test_text, (x, y))


def show_image(image, x, y):
    screen.blit(image, (x, y))


def background():
    screen.blit(active_background, (0, 0))

# initiates pygame
pygame.init()

# Screen
width = 1200
height = 675
screen = pygame.display.set_mode((width, height))



# Title and Window
pygame.display.set_caption("Test Caption")
# icon = pygame.image.load("")
# pygame.display.set_icon(icon)



# Fonts
font_alagard = pygame.font.Font("Fonts/alagard.ttf", 100)



# backgrounds
main_menu_background = pygame.image.load("Images/Start bild.png")
main_menu_background = pygame.transform.scale(main_menu_background, (width, height))


main_room = pygame.image.load('Images/main room.png')
main_room = pygame.transform.scale(main_room, (width, height))

active_background = main_menu_background




# images
small_chest = pygame.image.load(("Images/Chest.png"))

inventory_image = pygame.image.load('Images/Inventory_slot.png')

door_image = pygame.image.load('Images/Dörr.png')

# making button images
inventory_button = Buttons.Button(inventory_image, 0, 0, 0.3)
door_button = Buttons.Button(door_image, 100, 100, 6)

# making button text
exit_button = TextButtons.TextButton(width-100, 25, 'X', 'red', 'Fonts/alagard.ttf')
new_game_button = TextButtons.TextButton(200, 200, 'New game', 'white', 'Fonts/alagard.ttf')




# hide/show buttons/images
show_new_game_button = True
show_door_button = False
# Game Loop
running = True
while running:

    screen.fill((60, 50, 217))
    # Graphics
    background()

    inventory_button.render_image(screen)
    if inventory_button.image_button():
        print('clicked')

    exit_button.render_text(screen)
    if exit_button.text_button():
        running = False

    if show_new_game_button == True:
        new_game_button.render_text(screen)
    if new_game_button.text_button():
        active_background = main_room
        show_new_game_button = False
        show_door_button = True

    if show_door_button == True:
        door_button.render_image(screen)
        if door_button.image_button():
            print(Door.random_room())



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()


