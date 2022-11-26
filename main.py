import Buttons
import Items
import Monster
import TextButtons
import Player

import random

import pygame

import Door

import time

# functions

def show_text(text, x, y, color, font):
    test_text = font.render(text, True, (color))
    screen.blit(test_text, (x, y))


def show_image(image, x, y, scale):
    width = image.get_width()
    height = image.get_height()
    image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    screen.blit(image, (x, y))


def background():
    screen.blit(active_background, (0, 0))


def frame():
    global selected_weapon_frame_x
    screen.blit(frame_image, (0, 0))

    # hp stat:
    show_text(f"HP: {Player.player.hp}/ {Player.player.hp}", 1020, 2, "white", font_alagard_small)

    # weapon icons:
    weapon_1_button.render_image(screen)
    weapon_2_button.render_image(screen)

    if weapon_1_button.image_button():
        selected_weapon_frame_x = 37.5
    elif weapon_2_button.image_button():
        selected_weapon_frame_x = 105

    show_image(goldframe, selected_weapon_frame_x, 0, 7.5)

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
font_alagard_big = pygame.font.Font("Fonts/alagard.ttf", 100)
font_alagard_small = pygame.font.Font("Fonts/alagard.ttf", 25)


# backgrounds
main_menu_background = pygame.image.load("Images/Start bild.png")
main_menu_background = pygame.transform.scale(main_menu_background, (width, height))


main_room = pygame.image.load('Images/main room.png')
main_room = pygame.transform.scale(main_room, (width, height))

active_background = main_menu_background

frame_image = pygame.image.load('Images/Frame.png')
frame_image = pygame.transform.scale(frame_image, (width, height))




# images
small_chest = pygame.image.load("Images/Chest.png")

inventory_image = pygame.image.load('Images/Inventory_slot.png')

door_image = pygame.image.load('Images/Door.png')

hole_image = pygame.image.load('Images/Hole.png')

spike_image = pygame.image.load('Images/spike_trap.png')

spider_image = pygame.image.load('Images/spindel_prot.png')

zombie_boss_image = pygame.image.load('Images/zombie_boss.png')

goldframe = pygame.image.load("Images/GoldFrame.png")


# making button images
inventory_button = Buttons.Button(inventory_image, 0, 0, 0.3)
door_button_1 = Buttons.Button(door_image, 100, 190, 6)
door_button_2 = Buttons.Button(door_image, 500, 190, 6)
door_button_3 = Buttons.Button(door_image, 900, 190, 6)
small_chest_button = Buttons.Button(small_chest, 565, 450, 6)
door_button_chest_room = Buttons.Button(door_image, 150, 190, 6)
door_button_monster_room = Buttons.Button(door_image, 600, 190, 6)
spider_button = Buttons.Button(spider_image, 100, 100, 3)
zombie_boss_button = Buttons.Button(zombie_boss_image, 450, 220, 6)
door_to_boss = Buttons.Button(door_image, 500, 190, 6)
# Frame buttons
weapon_1_button = Buttons.Button(Player.player.weapon_1.icon, 45, -4, 4)
weapon_2_button = Buttons.Button(Player.player.weapon_2.icon, 113, -4, 4)

# making button text
exit_button = TextButtons.TextButton(width-100, 60, 'X', 'red', 'Fonts/alagard.ttf')
new_game_button = TextButtons.TextButton(200, 200, 'New game', 'white', 'Fonts/alagard.ttf')




# variables
main_lobby = False
show_new_game_button = True
show_door_button = True
show_door_button_monster_room = True
show_door_button_chest_room = True
loot_text = None
show_boss_room = False
hide_boss_text = False


monster_is_dead = False
generate_monster = True
start_monster_room_counter = False
room_type = None
clock = pygame.time.Clock()

trap_room_counter = 0
chest_room_counter = 0
monster_room_counter = 0
room_counter = 0
#random.seed(21150294)

selected_weapon_frame_x = 105

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
        frame()
        exit_button.render_text(screen)

        door_button_1.render_image(screen)
        door_button_2.render_image(screen)
        door_button_3.render_image(screen)

        if show_door_button == True:
            if door_button_1.image_button() or door_button_2.image_button() or door_button_3.image_button():
                if room_counter < 5:
                    room_type = Door.random_room()
                show_door_button = False
                show_door_button_chest_room = True
                show_door_button_monster_room = True
                generate_monster = True
                monster_is_dead = False
                loot_text = False
                start_monster_room_counter = False
                show_boss_room = False
                hide_boss_text = False

                trap_room_counter = 0
                monster_room_counter = 0

    # trap room
    if room_type == 'trap':
        background()
        frame()

        exit_button.render_text(screen)
        if trap_room_counter <= 30:
            show_text("It's a Dead End", 300, 100, 'white', font_alagard_big)
        if trap_room_counter >= 40:
            show_text('A Trap Appears!', 250, 100, 'red', font_alagard_big)
            show_image(hole_image, 410, 500, 7)
        if trap_room_counter >= 40:
            show_image(spike_image, 450, 487, 7)
        if trap_room_counter >= 60:
            room_type = None
            show_door_button = True

            room_counter += 1
        trap_room_counter += 1


    # chest room
    if room_type == 'chest':
        background()
        frame()

        exit_button.render_text(screen)
        door_button_chest_room.render_image(screen)

        if show_door_button_chest_room == True:
            if door_button_chest_room.image_button():
                room_type = None
                show_door_button = True
                show_door_button_monster_room = False
                room_counter += 1
            small_chest_button.render_image(screen)

        if small_chest_button.image_button():
            loot_text = True

        if loot_text == True:
            show_text('You Found:...', 300, 100, 'white', font_alagard_big)


    # monster room
    if room_type == 'monster':

        background()
        frame()
        exit_button.render_text(screen)
        door_button_monster_room.render_image(screen)
        if show_door_button_monster_room == True:
            if door_button_monster_room.image_button():
                room_type = None
                show_door_button = True
                monster_room_counter = 0
                monster_type = None
                show_door_button_monster_room = False
                room_counter += 1


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
                show_text('You Killed The Monster', 100, 100, 'red', font_alagard_big)
        if start_monster_room_counter == True:
            monster_room_counter += 1


    # boss room

    if room_counter == 5:

        background()
        frame()
        exit_button.render_text(screen)

        if hide_boss_text == False:
            door_to_boss.render_image(screen)
            show_text('YOU FOUND THE BOSS', 80, 100, 'red', font_alagard_big)

        if door_to_boss.image_button():
            hide_boss_text = True
            show_boss_room = True


        if show_boss_room == True:
            if monster_is_dead == False:
                zombie_boss_button.render_image(screen)
            if zombie_boss_button.image_button():
                monster_is_dead = True
                start_monster_room_counter = True
            if monster_is_dead and monster_room_counter <= 30:
                show_text('You Killed the Boss!', 100, 100, 'red', font_alagard_big)
            if monster_room_counter >= 30:
                show_text('Moving Down 1 Floor', 100, 100, 'white', font_alagard_big)



            if monster_room_counter >= 50:
                room_counter = 0
                room_type = None
                show_door_button = True


        if start_monster_room_counter == True:
            monster_room_counter += 1



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()


