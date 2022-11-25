import Buttons
import Monster
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

spider_image = pygame.image.load('Images/spindel_prot.png')

# making button images
inventory_button = Buttons.Button(inventory_image, 0, 0, 0.3)
door_button_1 = Buttons.Button(door_image, 100, 190, 6)
door_button_2 = Buttons.Button(door_image, 500, 190, 6)
door_button_3 = Buttons.Button(door_image, 900, 190, 6)
small_chest_button = Buttons.Button(small_chest, 565, 450, 6)
door_button_chest_room = Buttons.Button(door_image, 150, 190, 6)
door_button_monster_room = Buttons.Button(door_image, 600, 190, 6)
spider_button = Buttons.Button(spider_image, 100, 100, 3)

# making button text
exit_button = TextButtons.TextButton(width-100, 25, 'X', 'red', 'Fonts/alagard.ttf')
new_game_button = TextButtons.TextButton(200, 200, 'New game', 'white', 'Fonts/alagard.ttf')




# variables
main_lobby = False
show_new_game_button = True
show_door_button = True
show_door_button_monster_room = True
show_door_button_chest_room = True
loot_text = None

monster_is_dead = False
generate_monster = True
start_monster_room_counter = False
room_type = None
clock = pygame.time.Clock()

trap_room_counter = 0
chest_room_counter = 0
monster_room_counter = 0
#random.seed(21150294)

running = True
# Game Loop
while running:
    clock.tick(60)

    screen.fill((60, 50, 217))
    # Graphics

    # menu
    background()

    exit_button.render_text(screen)
    if exit_button.text_button():
        running = False

    new_game_button.render_text(screen)
    if show_new_game_button == True:
        if new_game_button.text_button():
            active_background = main_room
            show_new_game_button = False
            main_lobby = True

    # main lobby

    if main_lobby == True:
        background()
        exit_button.render_text(screen)

        door_button_1.render_image(screen)
        door_button_2.render_image(screen)
        door_button_3.render_image(screen)

        if show_door_button == True:
            if door_button_1.image_button() or door_button_2.image_button() or door_button_3.image_button():
                room_type = Door.random_room()
                show_door_button = False
                show_door_button_chest_room = True
                show_door_button_monster_room = True
                generate_monster = True
                monster_room_counter = 0
                monster_is_dead = False
                loot_text = False
                start_monster_room_counter = False


    # trap room
    if room_type == 'trap':
        background()


        exit_button.render_text(screen)
        if trap_room_counter <= 60:
            show_text("It's a Dead End", 300, 100, 'white')
        if trap_room_counter >= 70:
            show_text('A Trap Appears!', 250, 100, 'red')
            show_image(hole_image, 410, 500, 7)
        if trap_room_counter >= 70:
            show_image(spike_image, 450 , 487, 7)
        trap_room_counter += 1
        if trap_room_counter >= 90:
            room_type = None
            show_door_button = True
            trap_room_counter = 0


    # chest room
    if room_type == 'chest':
        background()

        exit_button.render_text(screen)
        door_button_chest_room.render_image(screen)

        if show_door_button_chest_room == True:
            if door_button_chest_room.image_button():
                room_type = None
                show_door_button = True
                show_door_button_monster_room = False
            small_chest_button.render_image(screen)

        if small_chest_button.image_button():
            loot_text = True
        if loot_text == True:
            show_text('You Found:...', 300, 100, 'white')


    # monster room
    if room_type == 'monster':

        background()
        exit_button.render_text(screen)
        door_button_monster_room.render_image(screen)
        if show_door_button_monster_room == True:
            if door_button_monster_room.image_button():
                room_type = None
                show_door_button = True
                monster_room_counter = 0
                monster_type = None
                show_door_button_monster_room = False


        if generate_monster == True:
            monster_type = Monster.monster.type()
            generate_monster = False


        if monster_type == 'spindel':
            if monster_is_dead == False:
                spider_button.render_image(screen)
                if spider_button.image_button():
                    monster_is_dead = True
                    start_monster_room_counter = True
            if monster_is_dead == True and monster_room_counter <= 40:
                show_text('You Killed The Monster', 100, 100, 'red')
        if start_monster_room_counter == True:
            monster_room_counter += 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()


