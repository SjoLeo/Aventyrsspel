import Buttons
import Items
import Monster
import TextButtons
import Player
import LootChest
import random
import pygame
import sys
import Door
import time
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
    show_text(f"STR: {Player.player.strength}", 1020, 15, "white", font_alagard_small)

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


# initiates pygame
pygame.init()

# Screen
width = 1200
height = 675
screen = pygame.display.set_mode((width, height))


# Fonts
font_alagard_big = pygame.font.Font("Fonts/alagard.ttf", 100)
font_alagard_small = pygame.font.Font("Fonts/alagard.ttf", 15)

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
zombie_image = pygame.image.load('Images/zombie.png')

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
zombie_button = Buttons.Button(zombie_image, 300, 180, 5)
# Frame buttons
weapon_1_button = Buttons.Button(Player.player.weapon_1.icon, 45, -4, 4)
weapon_2_button = Buttons.Button(Player.player.weapon_2.icon, 113, -4, 4)

armour_1_button = Buttons.Button(Player.player.armour_1.icon, 215, 0, 4)
armour_2_button = Buttons.Button(Player.player.armour_2.icon, 283, 0, 4)

# making button text
exit_button = TextButtons.TextButton(width - 100, 60, 'X', 'red', 'Fonts/alagard.ttf')
new_game_button = TextButtons.TextButton(200, 200, 'New game', 'white', 'Fonts/alagard.ttf')

# variables

lootchest = None
monster_type = None
monster = None
room_type = None

tick_counter = 0
room_counter = 0

selected_weapon_frame_x = 37.5
selected_armour_frame_x = 210

clock = pygame.time.Clock()


class GameState():
    def __init__(self):
        self.state = 'start_game'

    def start_game(self):
        global active_background

        background()

        exit_button.render_text(screen)
        if exit_button.text_button():
            pygame.quit()
            sys.exit()


        new_game_button.render_text(screen)
        if new_game_button.text_button():
            active_background = main_room
            self.state = 'menu'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

    def menu(self):
        global room_type
        global room_counter
        global lootchest
        global monster
        global monster_type

        background()
        frame()
        exit_button.render_text(screen)
        if exit_button.text_button():
            pygame.quit()
            sys.exit()


        door_button_1.render_image(screen)
        door_button_2.render_image(screen)
        door_button_3.render_image(screen)

        if door_button_1.image_button() or door_button_2.image_button() or door_button_3.image_button():
            if room_counter < 5:
                room_type = Door.random_room()
                if room_type == 'monster':
                    monster = Monster.Monster()
                    monster_type = monster.monster_type()
                    self.state = 'monster_room'

                if room_type == 'chest':
                    lootchest = LootChest.LootChest()
                    self.state = 'chest_room'
                if room_type == 'trap':
                    self.state = 'trap_room'
            if room_counter == 5:
                self.state = 'room_to_boss_room'
        pygame.display.flip()

    def trap_room(self):
        global room_counter
        global tick_counter
        global room_type

        background()
        frame()

        exit_button.render_text(screen)
        if exit_button.text_button():
            pygame.quit()
            sys.exit()

        if tick_counter <= 20:
            show_text("It's a Dead End", 300, 100, 'white', font_alagard_big)
        if tick_counter >= 25:
            show_text('A Trap Appears!', 250, 100, 'red', font_alagard_big)
            show_image(hole_image, 410, 500, 7)
        if tick_counter >= 35:
            show_image(spike_image, 450, 487, 7)
        if tick_counter >= 50:
            room_counter += 1
            tick_counter = 0
            self.state = 'menu'

        tick_counter += 1

        pygame.display.flip()
    def chest_room(self):
        global room_counter

        background()
        frame()

        exit_button.render_text(screen)
        if exit_button.text_button():
            pygame.quit()
            sys.exit()
        door_button_chest_room.render_image(screen)

        if door_button_chest_room.image_button():
            room_counter += 1
            self.state = 'menu'

        small_chest_button.render_image(screen)

        if small_chest_button.image_button():
            self.state = 'chest_room_opened'

        pygame.display.flip()

    def chest_room_opened(self):
        global room_counter

        background()
        frame()

        exit_button.render_text(screen)
        if exit_button.text_button():
            pygame.quit()
            sys.exit()
        door_button_chest_room.render_image(screen)

        if door_button_chest_room.image_button():
            room_counter += 1
            self.state = 'menu'

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

        pygame.display.flip()

    def monster_room(self):
        global room_counter
        global monster
        global monster_type




        background()
        frame()
        exit_button.render_text(screen)
        if exit_button.text_button():
            pygame.quit()
            sys.exit()

        door_button_monster_room.render_image(screen)

        if door_button_monster_room.image_button():
            room_counter += 1
            self.state = 'menu'


        if monster_type == 'spindel':
            spider_button.render_image(screen)
            if spider_button.image_button():
                self.state = 'monster_room_killed'

        if monster_type == 'zombie':
            zombie_button.render_image(screen)
            if zombie_button.image_button():
                self.state = 'monster_room_killed'

    def monster_room_killed(self):
        global room_counter

        background()
        frame()
        exit_button.render_text(screen)
        if exit_button.text_button():
            pygame.quit()
            sys.exit()
        door_button_monster_room.render_image(screen)

        if door_button_monster_room.image_button():
            room_counter += 1
            self.state = 'menu'

        show_text('You Killed The Monster', 100, 100, 'red', font_alagard_big)

    def room_to_boss_room(self):
        background()
        frame()
        exit_button.render_text(screen)
        if exit_button.text_button():
            pygame.quit()
            sys.exit()

        door_to_boss.render_image(screen)
        show_text('YOU FOUND THE BOSS', 80, 100, 'red', font_alagard_big)

        if door_to_boss.image_button():
            self.state = 'boss_room'
    def boss_room(self):
        background()
        frame()
        exit_button.render_text(screen)
        if exit_button.text_button():
            pygame.quit()
            sys.exit()

        zombie_boss_button.render_image(screen)
        if zombie_boss_button.image_button():

            self.state = 'boss_room_killed'

    def boss_room_killed(self):
        global room_counter
        global tick_counter

        background()
        frame()
        exit_button.render_text(screen)
        if exit_button.text_button():
            pygame.quit()
            sys.exit()

        if tick_counter <= 30:
            show_text('You Killed the Boss!', 100, 100, 'red', font_alagard_big)
        if tick_counter >= 30:
            show_text('Moving Down 1 Floor', 100, 100, 'white', font_alagard_big)

        if tick_counter >= 50:
            room_counter = 0
            tick_counter = 0
            self.state = 'menu'
        tick_counter += 1

    def state_manager(self):
        if self.state == 'start_game':
            self.start_game()

        if self.state == 'menu':
            self.menu()

        if self.state == 'monster_room':
            self.monster_room()
        if self.state == 'monster_room_killed':
            self.monster_room_killed()

        if self.state == 'chest_room':
            self.chest_room()
        if self.state == 'chest_room_opened':
            self.chest_room_opened()

        if self.state == 'trap_room':
            self.trap_room()

        if self.state == 'room_to_boss_room':
            self.room_to_boss_room()

        if self.state == 'boss_room':
            self.boss_room()

        if self.state == 'boss_room_killed':
            self.boss_room_killed()