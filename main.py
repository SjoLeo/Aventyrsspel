import Buttons
import TextButtons

import random

import pygame

import Door

import time

# functions

def show_text(text, x, y, color):
    test_text = font_alagard.render(text, True, (color))
    screen.blit(test_text, (x, y))


def show_image(image, x, y, scale):
    width = image.get_width()
    height = image.get_height()
    image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
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

door_image = pygame.image.load('Images/Door.png')

hole_image = pygame.image.load('Images/Hole.png')

spike_image = pygame.image.load('Images/spike_trap.png')

# making button images
inventory_button = Buttons.Button(inventory_image, 0, 0, 0.3)
door_button_1 = Buttons.Button(door_image, 100, 190, 6)
door_button_2 = Buttons.Button(door_image, 500, 190, 6)
door_button_3 = Buttons.Button(door_image, 900, 190, 6)
# making button text
exit_button = TextButtons.TextButton(width-100, 25, 'X', 'red', 'Fonts/alagard.ttf')
new_game_button = TextButtons.TextButton(200, 200, 'New game', 'white', 'Fonts/alagard.ttf')




# hide/show buttons/images
show_new_game_button = True
show_door_button = False
show_spike_image = True
# Game Loop
running = True

room_type = None
clock = pygame.time.Clock()

counter = 0
# random.seed(69)
while running:
    clock.tick(60)

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
        door_button_1.render_image(screen)
        door_button_2.render_image(screen)
        door_button_3.render_image(screen)
        if door_button_1.image_button() or door_button_2.image_button() or door_button_3.image_button():
            room_type = Door.random_room()
            #show_door_button = False


    # trap room
    if room_type == 'trap':
        background()


        exit_button.render_text(screen)
        if counter >= 5:
            show_image(hole_image, 410, 500, 7)
        if counter >= 10:
            show_image(spike_image, 450 , 487, 7)
        counter += 1








    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()


