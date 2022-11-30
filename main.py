import Buttons
import Items
import Monster
import TextButtons
import Player
import LootChest

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
    global selected_armour_frame_x
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

    show_image(gold_frame_image, selected_weapon_frame_x, 0, 7.5)

    # armour icons:
    armour_1_button.render_image(screen)
    armour_2_button.render_image(screen)

    if armour_1_button.image_button():
        selected_armour_frame_x = 210
    elif armour_2_button.image_button():
        selected_armour_frame_x = 278
    show_image(gold_frame_image, selected_armour_frame_x, 0, 7.5)

    # Potions
    potion_1_button.render_image(screen)
    potion_2_button.render_image(screen)
    drink_button.render_image(screen)



    # Progress Bar

    # 7.5 pixels per bakgrundspixel
    # +98 x pixels per room (verkar vara nåt konstigt som gör det inconsistent)
    # (borde gå att göra mer clean med nån class eller nåt)
    if room_counter > 0:
        show_image(green_progress, 570, 600, 10)

    if room_counter > 1:
        show_image(green_progress, 668, 600, 10)

    if room_counter > 2:
        show_image(green_progress, 765, 600, 10)

    if room_counter > 3:
        show_image(green_progress, 863, 600, 10)

    if room_counter > 4:
        show_image(green_progress, 960, 600, 10)


def reset_variables():
    global show_door_button
    global show_room_exit
    global show_chest
    global generate_monster
    global monster_is_dead
    global show_room_text
    global hide_room_text
    global show_boss_room
    global start_tick_counter
    global monster_type
    global lootchest
    global generate_loot_chest
    global tick_counter

    show_door_button = False
    show_room_exit = True
    show_chest = True
    generate_monster = True
    monster_is_dead = False
    show_room_text = False
    hide_room_text = True
    show_boss_room = False
    start_tick_counter = False
    monster_type = None
    lootchest = None
    generate_loot_chest = True
    tick_counter = 0


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

gold_frame_image = pygame.image.load("Images/GoldFrame.png")

open_chest_image = pygame.image.load("Images/open_chest.png")

chest_item_frame_image = pygame.image.load("Images/chest_loot_frame.png")

green_progress = pygame.image.load("Images/green.png")

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

armour_1_button = Buttons.Button(Player.player.armour_1.icon, 215, 0, 4)
armour_2_button = Buttons.Button(Player.player.armour_2.icon, 283, 0, 4)

# making button text
exit_button = TextButtons.TextButton(width - 100, 60, 'X', 'red', 'Fonts/alagard.ttf')
new_game_button = TextButtons.TextButton(200, 200, 'New game', 'white', 'Fonts/alagard.ttf')

# variables
main_lobby = False
show_new_game_button = True
show_door_button = True
show_room_exit = True

show_room_text = False
show_boss_room = False
generate_loot_chest = True
show_chest = True

monster_is_dead = False
generate_monster = True
start_tick_counter = False
room_type = None

clock = pygame.time.Clock()

tick_counter = 0
chest_room_counter = 0

room_counter = 0

pos = None

random.seed(69)

selected_weapon_frame_x = 37.5
selected_armour_frame_x = 210

running = True

# Game Loop
while running:
    # pos = pygame.mouse.get_pos()
    # print(pos)
    clock.tick(60)

    screen.fill((60, 50, 217))
    # Graphics

    # menu
    background()

    exit_button.render_text(screen)
    if exit_button.text_button():
        running = False

    new_game_button.render_text(screen)
    if show_new_game_button:
        if new_game_button.text_button():
            active_background = main_room
            show_new_game_button = False
            main_lobby = True

    # main lobby

    if main_lobby:
        background()
        frame()
        exit_button.render_text(screen)

        door_button_1.render_image(screen)
        door_button_2.render_image(screen)
        door_button_3.render_image(screen)

        if show_door_button:
            if door_button_1.image_button() or door_button_2.image_button() or door_button_3.image_button():
                if room_counter < 5:
                    room_type = Door.random_room()
                reset_variables()

    # trap room

    if room_type == 'trap':
        background()
        frame()

        exit_button.render_text(screen)
        if tick_counter <= 20:
            show_text("It's a Dead End", 300, 100, 'white', font_alagard_big)
        if tick_counter >= 25:
            show_text('A Trap Appears!', 250, 100, 'red', font_alagard_big)
            show_image(hole_image, 410, 500, 7)
        if tick_counter >= 35:
            show_image(spike_image, 450, 487, 7)
        if tick_counter >= 50:
            room_type = None
            show_door_button = True

            room_counter += 1
        tick_counter += 1

    # chest room
    if room_type == 'chest':
        background()
        frame()
        if generate_loot_chest:
            lootchest = LootChest.LootChest()
            generate_loot_chest = False

        exit_button.render_text(screen)
        door_button_chest_room.render_image(screen)

        if show_room_exit:
            if door_button_chest_room.image_button():
                room_type = None
                show_door_button = True
                show_room_exit = False
                room_counter += 1

        if show_chest:
            small_chest_button.render_image(screen)

        if small_chest_button.image_button():
            show_chest = False

            show_room_text = True

        if show_room_text:
            show_text('You Found:...', 300, 100, 'white', font_alagard_big)
            show_image(open_chest_image, 565, 426, 6)
            show_image(chest_item_frame_image, 468, 257, 4)
            show_text("Choose One", 500, 270, "white", font_alagard_small)

            item1 = lootchest.items[0]
            show_image(item1.icon, 513, 300, 4)

            item2 = lootchest.items[1]
            show_image(item2.icon, 600, 300, 4)

            item3 = lootchest.items[2]
            show_image(item3.icon, 687, 300, 4)

    # monster room
    if room_type == 'monster':

        background()
        frame()
        exit_button.render_text(screen)
        door_button_monster_room.render_image(screen)
        if show_room_exit:
            if door_button_monster_room.image_button():
                room_type = None
                show_door_button = True
                room_counter += 1

        if generate_monster:
            monster_type = Monster.monster.type()
            generate_monster = False

        if monster_type == 'spindel':
            if not monster_is_dead:
                spider_button.render_image(screen)
                if spider_button.image_button():
                    monster_is_dead = True
                    start_tick_counter = True
            if monster_is_dead == True and tick_counter <= 40:
                show_text('You Killed The Monster', 100, 100, 'red', font_alagard_big)
        if start_tick_counter:
            tick_counter += 1

    # boss room

    if room_counter == 5:

        background()
        frame()
        exit_button.render_text(screen)

        if hide_room_text == True:
            door_to_boss.render_image(screen)
            show_text('YOU FOUND THE BOSS', 80, 100, 'red', font_alagard_big)

        if door_to_boss.image_button():
            hide_room_text = False
            show_boss_room = True

        if show_boss_room:
            if not monster_is_dead:
                zombie_boss_button.render_image(screen)
            if zombie_boss_button.image_button():
                monster_is_dead = True
                start_tick_counter = True
            if monster_is_dead and tick_counter <= 30:
                show_text('You Killed the Boss!', 100, 100, 'red', font_alagard_big)
            if tick_counter >= 30:
                show_text('Moving Down 1 Floor', 100, 100, 'white', font_alagard_big)

            if tick_counter >= 50:
                room_counter = 0
                room_type = None
                show_door_button = True

        if start_tick_counter:
            tick_counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
