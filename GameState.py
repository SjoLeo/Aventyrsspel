import Animation
import Buttons
import Items
import Monster
import TextButtons
import Player

import random
import pygame
import sys
import copy

import time

import Worldinfo


def show_text(text, x, y, color, font):
    test_text = font.render(text, True, color)
    screen.blit(test_text, (x, y))


def random_item():
    # randomize stats for items
    # makes copy
    random_items_list = copy.deepcopy((random.choice(random.choice(Items.items_list)),
                                       random.choice(random.choice(Items.items_list)),
                                       random.choice(random.choice(Items.items_list))))
    for item in random_items_list:

        if item.type == 'weapon':
            item.strength = random.randint(3, 10) * Worldinfo.current_dungeon_floor

        if item.type == 'armour':
            item.defence = random.randint(1, 3) * Worldinfo.current_dungeon_floor

    return random_items_list


def show_image(image, x, y, scale):
    width = image.get_width()
    height = image.get_height()
    image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    return screen.blit(image, (x, y))


def background():
    screen.blit(active_background, (0, 0))


def random_room():
    rooms = ['monster', 'trap', 'chest']
    return random.choice(rooms)


def draw_inventory_hovering_image(pop_up_rect_x):
    global pop_up_rect_y
    pop_up_rect_y = 67
    pop_up_rect_width = 60
    pop_up_rect_height = 20

    pygame.draw.rect(screen, (255, 255, 255), (pop_up_rect_x, pop_up_rect_y, pop_up_rect_width, pop_up_rect_height))
    pygame.draw.rect(screen, (0, 0, 0),
                     (pop_up_rect_x + 1, pop_up_rect_y + 1, pop_up_rect_width - 2, pop_up_rect_height - 2))


def frame():
    global selected_weapon_frame_x
    global selected_armour_frame_x
    global selected_potion_frame_x
    global inventory_input

    if Player.player.current_hp <= 3:
        show_image(red_fade_small_image, 0, 0, 7.5)

    screen.blit(frame_image, (0, 0))

    # displayed stats:
    show_text(f"HP: {Player.player.current_hp}/ {Player.player.hp}", 1020, 2, "white", font_alagard_small)

    if type_of_room == 'mini_boss' or type_of_room == 'final_boss':
        if Player.player.current_combo != 1:
            show_text(f"STR: {int(Player.player.damage / Player.player.current_combo)} x {Player.player.current_combo}",
                      1020, 15, "white", font_alagard_small)
        else:
            show_text(f"STR: {Player.player.damage}", 1020, 15, "white", font_alagard_small)
    else:
        if Player.player.damage_multiplier != 1 and not Player.player.weapon_inventory[
                                                            Player.player.equipped_weapon] == 'Empty':
            show_text(
                f"STR: {Player.player.damage - Player.player.weapon_inventory[Player.player.equipped_weapon].strength} + {Player.player.weapon_inventory[Player.player.equipped_weapon].strength}",
                1020, 15, "white", font_alagard_small)
        else:
            show_text(f"STR: {Player.player.damage}", 1020, 15, "white", font_alagard_small)

    show_text(f"DEF: {Player.player.total_defence}", 1020, 28, "white", font_alagard_small)
    show_text(f'Player level: {Player.player.lvl}', 546, 10, 'white', font_alagard_medium)
    show_text(f'Dungeon floor: {Worldinfo.current_dungeon_floor}', 546, 30, 'white', font_alagard_medium)

    # show weapon icons
    if not Player.player.weapon_inventory[0] == 'Empty':
        show_image(Player.player.weapon_inventory[0].icon, 45, -4, 4)
    if not Player.player.weapon_inventory[1] == 'Empty':
        show_image(Player.player.weapon_inventory[1].icon, 113, -4, 4)

    # clickable slots
    if empty_inv_button1.got_pressed() or inventory_input == 1:
        selected_weapon_frame_x = 37.5
        Player.player.equipped_weapon = 0

    elif empty_inv_button2.got_pressed() or inventory_input == 2:
        selected_weapon_frame_x = 105
        Player.player.equipped_weapon = 1

    show_image(gold_frame_image, selected_weapon_frame_x, 0, 7.5)

    # show armour icons
    if not Player.player.armour_inventory[0] == 'Empty':
        show_image(Player.player.armour_inventory[0].icon, 215, 0, 4)
    if not Player.player.armour_inventory[1] == 'Empty':
        show_image(Player.player.armour_inventory[1].icon, 283, 0, 4)

    # clickable slots
    if empty_inv_button3.got_pressed() or inventory_input == 3:
        selected_armour_frame_x = 210
        Player.player.equipped_armour = 0

    elif empty_inv_button4.got_pressed() or inventory_input == 4:
        selected_armour_frame_x = 278
        Player.player.equipped_armour = 1

    show_image(gold_frame_image, selected_armour_frame_x, 0, 7.5)

    # show potion icon
    if not Player.player.potion_inventory[0] == 'Empty':
        show_image(Player.player.potion_inventory[0].icon, 390, -4, 4)
    if not Player.player.potion_inventory[1] == 'Empty':
        show_image(Player.player.potion_inventory[1].icon, 458, -4, 4)

    # clickable slots
    if empty_inv_button5.got_pressed() or inventory_input == 5:
        selected_potion_frame_x = 383
        Player.player.equipped_potion = 0
    elif empty_inv_button6.got_pressed() or inventory_input == 6:
        selected_potion_frame_x = 451
        Player.player.equipped_potion = 1
    show_image(gold_frame_image, selected_potion_frame_x, 0, 7.5)

    # ======= hovering over slots ========

    if empty_inv_button1.mouse_hover() and not Player.player.weapon_inventory[0] == 'Empty':
        pop_up_rect_x = 45
        draw_inventory_hovering_image(pop_up_rect_x)
        show_text(f'STR: {Player.player.weapon_inventory[0].strength}', pop_up_rect_x + 3, pop_up_rect_y + 3, 'white',
                  font_alagard_small)
    if empty_inv_button2.mouse_hover() and not Player.player.weapon_inventory[1] == 'Empty':
        pop_up_rect_x = 112
        draw_inventory_hovering_image(pop_up_rect_x)
        show_text(f'STR: {Player.player.weapon_inventory[1].strength}', pop_up_rect_x + 3, pop_up_rect_y + 3, 'white',
                  font_alagard_small)

    if empty_inv_button3.mouse_hover() and not Player.player.armour_inventory[0] == 'Empty':
        pop_up_rect_x = 218
        draw_inventory_hovering_image(pop_up_rect_x)
        show_text(f'DEF: {Player.player.armour_inventory[0].defence}', pop_up_rect_x + 3, pop_up_rect_y + 3, 'white',
                  font_alagard_small)
    if empty_inv_button4.mouse_hover() and not Player.player.armour_inventory[1] == 'Empty':
        pop_up_rect_x = 285
        draw_inventory_hovering_image(pop_up_rect_x)
        show_text(f'DEF: {Player.player.armour_inventory[1].defence}', pop_up_rect_x + 3, pop_up_rect_y + 3, 'white',
                  font_alagard_small)

    if empty_inv_button5.mouse_hover() and not Player.player.potion_inventory[0] == 'Empty':
        pop_up_rect_x = 391
        draw_inventory_hovering_image(pop_up_rect_x)
        if Player.player.potion_inventory[0].name == 'Potion_of_health':
            show_text('HP: +3', pop_up_rect_x + 3, pop_up_rect_y + 3, 'white', font_alagard_small)
    if empty_inv_button6.mouse_hover() and not Player.player.potion_inventory[1] == 'Empty':
        pop_up_rect_x = 458
        draw_inventory_hovering_image(pop_up_rect_x)
        if Player.player.potion_inventory[1].name == 'Potion_of_health':
            show_text('HP: +3', pop_up_rect_x + 3, pop_up_rect_y + 3, 'white', font_alagard_small)

    # ======Dungeon Progress Bar======

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

    # ====== EXP ======

    exp_percentage = Player.player.exp / Player.player.level_up_exp

    exp_bar_x = 780
    exp_bar_y = 35
    exp_bar_width = 200
    exp_bar_height = 20

    # outer rectangle
    pygame.draw.rect(screen, (255, 255, 255), (exp_bar_x, exp_bar_y, exp_bar_width, exp_bar_height))
    # inner rectangle
    pygame.draw.rect(screen, (0, 0, 0), (exp_bar_x + 1, exp_bar_y + 1, exp_bar_width - 2, exp_bar_height - 2))

    # extra stats gets added in this function
    Player.player.calculate_exp_overflow()

    # exp progress
    if exp_percentage < 1:
        pygame.draw.rect(screen, (209, 133, 46),
                         (exp_bar_x + 1, exp_bar_y + 1, int((exp_bar_width - 2) * exp_percentage), exp_bar_height - 2))
    else:
        pygame.draw.rect(screen, (209, 133, 46),
                         (exp_bar_x + 1, exp_bar_y + 1, (exp_bar_width - 2), exp_bar_height - 2))

    show_text('EXP', exp_bar_x + 75, exp_bar_y - 25, 'white', font_alagard_medium)


# initiates pygame
pygame.init()

# Screen
width = 1200
height = 675
screen = pygame.display.set_mode((width, height))

# Fonts
font_alagard_huge = pygame.font.Font('Fonts/alagard.ttf', 150)
font_alagard_big = pygame.font.Font("Fonts/alagard.ttf", 70)
font_alagard_small = pygame.font.Font("Fonts/alagard.ttf", 15)
font_alagard_medium = pygame.font.Font('Fonts/alagard.ttf', 25)
font_alagard_medium_big = pygame.font.Font('Fonts/alagard.ttf', 50)

# backgrounds
main_menu_background = pygame.image.load("Images/Start bild.png")
main_menu_background = pygame.transform.scale(main_menu_background, (width, height))

main_room = pygame.image.load('Images/main room.png')
main_room = pygame.transform.scale(main_room, (width, height))

boss_room = pygame.image.load('Images/Boss_room.png')
boss_room = pygame.transform.scale(boss_room, (width, height))

ending_background = pygame.image.load('Images/ending_background.png')
ending_background = pygame.transform.scale(ending_background, (width, height))

active_background = main_menu_background

frame_image = pygame.image.load('Images/Frame.png')
frame_image = pygame.transform.scale(frame_image, (width, height))

# images
small_chest = pygame.image.load("Images/Chest.png")
door_image = pygame.image.load('Images/Door.png')
hole_image = pygame.image.load('Images/Hole.png')
spike_image = pygame.image.load('Images/spike_trap.png')
gold_frame_image = pygame.image.load("Images/GoldFrame.png")
open_chest_image = pygame.image.load("Images/open_chest.png")
chest_item_frame_image = pygame.image.load("Images/chest_loot_frame.png")
green_progress = pygame.image.load("Images/green.png")
empty_inv_image = pygame.image.load('Images/empty_inv.png')
torch_image = pygame.image.load('Images/torch.png')
darkness_image = pygame.image.load("Images/Darkness.png")
darkness_small_image = pygame.image.load("Images/Darkness_small.png")
vulnerable_spot_image = pygame.image.load('Images/vulnerable_spot.png')
red_fade_small_image = pygame.image.load("Images/Red_fade_small.png")

zombie_image = pygame.image.load('Images/zombie.png')
spider_image = pygame.image.load('Images/spindel_prot.png')
goblin_image = pygame.image.load("Images/goblin.png")

final_boss_image = pygame.image.load('Images/Final_boss.png')
mimic_image = pygame.image.load("Images/Mimic.png")
final_boss_door = pygame.image.load('Images/final_boss_door.png')

taking_damage_image = pygame.image.load('Images/taking_damage_image.png')
empty_background_image = pygame.image.load('Images/empty_background.png')

# making button images
door_button_1 = Buttons.Button(door_image, 100, 190, 6)
door_button_2 = Buttons.Button(door_image, 500, 190, 6)
door_button_3 = Buttons.Button(door_image, 900, 190, 6)
small_chest_button = Buttons.Button(small_chest, 565, 450, 6)
door_button_chest_room = Buttons.Button(door_image, 150, 190, 6)
door_button_monster_room = Buttons.Button(door_image, 600, 190, 6)
door_to_boss = Buttons.Button(door_image, 500, 190, 6)
final_boss_door_button = Buttons.Button(final_boss_door, 539, 285, 7.5)

# monster buttons
# x and y changes in gamestate
spider_button = Buttons.Button(spider_image, 0, 0, 3)
zombie_button = Buttons.Button(zombie_image, 0, 0, 5)
goblin_button = Buttons.Button(goblin_image, 0, 0, 4)




final_boss_x = 470
final_boss_y = 180

# vulnerable spot button
# x and y changes in gamestate
vulnerable_spot_button = Buttons.Button(vulnerable_spot_image, 0, 0, 4)

# frame buttons
empty_inv_button1 = Buttons.Button(empty_inv_image, 45, 0, 1)
empty_inv_button2 = Buttons.Button(empty_inv_image, 113, 0, 1)

empty_inv_button3 = Buttons.Button(empty_inv_image, 215, 0, 1)
empty_inv_button4 = Buttons.Button(empty_inv_image, 283, 0, 1)

empty_inv_button5 = Buttons.Button(empty_inv_image, 390, 0, 1)
empty_inv_button6 = Buttons.Button(empty_inv_image, 458, 0, 1)

# making button text
exit_button = TextButtons.TextButton(width - 100, 80, 'X', 'red', 'Fonts/alagard.ttf', 100)
new_game_button = TextButtons.TextButton(150, 100, 'New game', 'yellow', 'Fonts/alagard.ttf', 100)
tutorial_button = TextButtons.TextButton(200, 200, "Tutorial", "white", "Fonts/alagard.ttf", 100)
credits_button = TextButtons.TextButton(270, 300, "Credits", "white", "Fonts/alagard.ttf", 100)
back_button = TextButtons.TextButton(700, 70, "Back", "red", "Fonts/alagard.ttf", 50)

# variables

monster_type = None
room_type = None

tick_counter = 0
room_counter = 0
image_alpha = 0
inventory_input = 0
type_of_room = None

selected_weapon_frame_x = 37.5
selected_armour_frame_x = 210
selected_potion_frame_x = 383

boss_scale = 6
boss_x = 450
boss_y = 220

clock = pygame.time.Clock()


class GameState():
    def __init__(self):
        self.state = 'start_game'

    def start_game(self):
        global active_background

        background()
        new_game_button.render_text(screen)
        tutorial_button.render_text(screen)
        credits_button.render_text(screen)

        if new_game_button.text_button():
            active_background = main_room
            self.state = 'menu'

        if tutorial_button.text_button():
            self.state = "tutorial"

        if credits_button.text_button():
            self.state = "credits"

    def tutorial(self):
        background()

        back_button.render_text(screen)
        if back_button.text_button():
            self.state = 'start_game'

        show_text("Tutorial", 50, 45, "yellow", font_alagard_big)
        show_text("You set foot in in a treacherous dungeon in hopes of treasure,",
                  30, 120, "white", font_alagard_medium)
        show_text("glory and slaying the unholy beasts who call this crypt their home.",
                  30, 150, "white", font_alagard_medium)

        show_text("Your goal is to get deep below ground to at least floor 10 and cut down",
                  30, 210, "white", font_alagard_medium)
        show_text("the abominable warden to escape.", 30, 240, "white", font_alagard_medium)

    def credits(self):
        background()

        back_button.render_text(screen)
        if back_button.text_button():
            self.state = 'start_game'

        show_text("Credits", 50, 45, "yellow", font_alagard_big)
        show_text("A game made by:", 270, 120, "white", font_alagard_medium_big)

        show_text("Leo Sjostrom", 260, 200, (252, 173, 3), font_alagard_big)
        show_text("Isak Wadelius", 270, 270, (0, 124, 212), font_alagard_big)
        show_text("Leo Nordstrand", 280, 340, (147, 6, 194), font_alagard_big)
        show_text("..", 441, 162, (252, 173, 3), font_alagard_big)
        show_text("..", 568, 162, (252, 173, 3), font_alagard_big)

    def menu(self):
        global room_type, room_counter, monster, monster_type, monster_x, monster_y, type_of_room

        if Worldinfo.current_dungeon_floor >= 10:
            self.state = 'menu_with_final_boss'

        background()
        frame()

        door_button_1.render_image(screen)
        door_button_2.render_image(screen)
        door_button_3.render_image(screen)

        if door_button_1.got_pressed() or door_button_2.got_pressed() or door_button_3.got_pressed():
            if room_counter < 5:
                room_type = random_room()
                type_of_room = room_type
                if room_type == 'monster':
                    monster = Monster.Monster()
                    monster_type = monster.type
                    monster_x = monster.monster_position()[0]
                    monster_y = monster.monster_position()[1]
                    self.state = 'monster_room'

                if room_type == 'chest':
                    self.state = 'chest_room'

                if room_type == 'trap':
                    self.state = random.choice(['mimic_room', 'spike_room'])

            if room_counter == 5:
                self.state = 'room_to_boss_room'

    def menu_with_final_boss(self):
        global room_type, room_counter, monster, monster_type, monster_x, monster_y
        background()
        frame()

        door_button_1.render_image(screen)
        door_button_2.render_image(screen)
        door_button_3.render_image(screen)
        show_image(torch_image, 840, 240, 5)
        show_image(torch_image, 1120, 240, 5)

        if door_button_1.got_pressed() or door_button_2.got_pressed():
            if room_counter < 5:
                room_type = random_room()
                print(room_type)
                if room_type == 'monster':
                    monster = Monster.Monster()
                    monster_type = monster.type
                    monster_x = monster.monster_position()[0]
                    monster_y = monster.monster_position()[1]

                    self.state = 'monster_room'

                if room_type == 'chest':
                    self.state = 'chest_room'

                if room_type == 'trap':
                    self.state = 'trap_room'

            if room_counter == 5:
                self.state = 'room_to_boss_room'

        if door_button_3.got_pressed():
            self.state = 'final_boss'

    def spike_room(self):
        global room_counter, tick_counter, room_type

        background()
        frame()

        if tick_counter <= 20:
            show_text("It's a Dead End", 150, 120, 'white', font_alagard_big)
        elif tick_counter >= 25:
            show_text('A Trap Appears!', 150, 120, 'red', font_alagard_big)
            show_image(hole_image, 410, 500, 7)
        if tick_counter >= 35:
            show_image(spike_image, 450, 487, 7)

        if tick_counter >= 50:
            # player takes damage
            Player.player.current_hp -= 1
            room_counter += 1
            tick_counter = 0
            Worldinfo.traps_triggered += 1
            self.state = 'menu'

        tick_counter += self.dt * 30

    def mimic_room(self):
        global room_counter, tick_counter

        background()
        frame()

        small_chest_button.render_image(screen)

        door_button_chest_room.render_image(screen)

        if door_button_chest_room.got_pressed():
            room_counter += 1
            self.state = 'menu'

        if small_chest_button.got_pressed():
            self.state = 'mimic_room_opened'

    def mimic_room_opened(self):
        global tick_counter, room_counter
        background()
        frame()

        show_image(mimic_image, 565, 426, 6)
        show_text("It's a Trap!", 150, 120, 'red', font_alagard_big)

        door_button_chest_room.render_image(screen)
        if door_button_chest_room.got_pressed():
            tick_counter = 0
            room_counter += 1
            Player.player.current_hp -= 1
            self.state = 'menu'

        if tick_counter >= 60:
            # player takes damage
            Player.player.current_hp -= 1
            room_counter += 1
            tick_counter = 0
            Worldinfo.traps_triggered += 1
            self.state = 'menu'

        tick_counter += self.dt * 30

    def chest_room(self):
        global room_counter, random_items, item1_chest_button, item2_chest_button, item3_chest_button

        background()
        frame()

        door_button_chest_room.render_image(screen)

        if door_button_chest_room.got_pressed():
            room_counter += 1
            self.state = 'menu'

        small_chest_button.render_image(screen)

        if small_chest_button.got_pressed():
            random_items = random_item()
            item1_chest_button = Buttons.Button(random_items[0].icon, 513, 300, 4)
            item2_chest_button = Buttons.Button(random_items[1].icon, 600, 300, 4)
            item3_chest_button = Buttons.Button(random_items[2].icon, 687, 300, 4)
            Worldinfo.chests_opened += 1
            self.state = 'chest_room_opened'

    def chest_room_opened(self):
        global room_counter

        background()
        frame()

        door_button_chest_room.render_image(screen)

        if door_button_chest_room.got_pressed():
            room_counter += 1

            self.state = 'menu'

        show_text('You Found:...', 150, 120, 'white', font_alagard_big)
        show_image(open_chest_image, 565, 426, 6)
        show_image(chest_item_frame_image, 468, 257, 4)
        show_text("Choose One", 500, 270, "white", font_alagard_small)

        item1_chest_button.render_image(screen)
        if item1_chest_button.got_pressed():
            Player.player.add_item_to_inventory(random_items[0])
            room_counter += 1

            self.state = 'menu'

        item2_chest_button.render_image(screen)
        if item2_chest_button.got_pressed():
            Player.player.add_item_to_inventory(random_items[1])
            room_counter += 1

            self.state = 'menu'

        item3_chest_button.render_image(screen)
        if item3_chest_button.got_pressed():
            Player.player.add_item_to_inventory(random_items[2])
            room_counter += 1

            self.state = 'menu'

    def monster_room(self):
        global room_counter, monster_type

        background()
        frame()
        # print(Player.player.damage)

        door_button_monster_room.render_image(screen)

        if door_button_monster_room.got_pressed():
            room_counter += 1
            monster_type = None
            self.state = 'menu'

        if monster_type == 'spider':
            spider_button.rect.x = monster_x
            spider_button.rect.y = monster_y
            spider_button.render_image(screen)
            if spider_button.got_pressed():
                self.state = 'fight'

        if monster_type == 'zombie':
            zombie_button.rect.x = monster_x
            zombie_button.rect.y = monster_y
            zombie_button.render_image(screen)
            if zombie_button.got_pressed():
                self.state = 'fight'

        if monster_type == 'goblin':
            goblin_button.rect.x = monster_x
            goblin_button.rect.y = monster_y
            goblin_button.render_image(screen)
            if goblin_button.got_pressed():
                self.state = 'fight'

    def fight(self):
        global monster_type
        if Player.player.damage > monster.strength:
            Player.player.exp += random.randint(40, 70)

            self.state = 'monster_room_killed'

        elif Player.player.damage == monster.strength:
            self.state = 'monster_room_tie'

        else:
            Player.player.current_hp -= 1
            self.state = 'monster_room_loss'

        monster_type = None

    def monster_room_killed(self):
        global room_counter

        background()
        frame()

        door_button_monster_room.render_image(screen)

        if door_button_monster_room.got_pressed():
            room_counter += 1
            Worldinfo.monsters_slayed += 1
            self.state = 'menu'

        show_text('You Killed The Monster', 150, 120, 'white', font_alagard_big)

    def monster_room_tie(self):
        global room_counter

        background()
        frame()

        door_button_monster_room.render_image(screen)
        if door_button_monster_room.got_pressed():
            room_counter += 1
            self.state = 'menu'

        show_text('You were of equal strength', 150, 120, 'white', font_alagard_big)

    def monster_room_loss(self):
        global room_counter

        background()
        frame()

        door_button_monster_room.render_image(screen)
        if door_button_monster_room.got_pressed():
            room_counter += 1
            self.state = 'menu'

        show_text('You lost to the monster', 150, 120, 'red', font_alagard_big)

    def room_to_boss_room(self):
        global active_background, boss, vulnerable_spot_x, vulnerable_spot_y, empty_background_button, type_of_room
        background()
        frame()

        door_to_boss.render_image(screen)
        show_text('YOU FOUND THE BOSS', 150, 120, 'red', font_alagard_big)
        show_image(torch_image, 420, 240, 5)
        show_image(torch_image, 740, 240, 5)

        if door_to_boss.got_pressed():
            active_background = boss_room
            # creates the boss object
            boss = Monster.Boss(100, False)

            # generate the first spot
            boss.generate_vulnerable_spot_coordinates(boss.image, boss_x, boss_y,
                                                      boss_scale)
            empty_background_button = Buttons.Button(empty_background_image, boss_x - 95, boss_y - 60,
                                                     13)
            type_of_room = 'mini_boss'

            self.state = 'boss_room'

    def boss_room(self):

        background()
        frame()

        boss.draw_health_bar(screen, boss_x + 10, boss_y - 50)
        show_text(f'COMBO: x{Player.player.current_combo}', 100, 120, 'white', font_alagard_big)

        show_image(boss.image, boss_x, boss_y, boss_scale)
        empty_background_button.render_image(screen)

        vulnerable_spot_button.rect.x = boss.vulnerable_x_coordinate
        vulnerable_spot_button.rect.y = boss.vulnerable_y_coordinate
        vulnerable_spot_button.render_image(screen)

        if vulnerable_spot_button.got_pressed():
            result = random.choice(['dodge', 'hit', 'hit', 'hit', 'hit'])
            if result == 'hit':
                boss.current_hp -= Player.player.damage
                # generate new spots
                boss.generate_vulnerable_spot_coordinates(boss.image, boss_x, boss_y,
                                                          boss_scale)
                Player.player.current_combo += 1
                # update the damage stats

            else:
                boss.generate_vulnerable_spot_coordinates(boss.image, boss_x, boss_y,
                                                          boss_scale)
                Player.player.current_hp -= 1
                Player.player.current_combo = 1

                self.state = 'boss_dodged'

        if empty_background_button.got_pressed() and not vulnerable_spot_button.mouse_hover():
            Player.player.current_hp -= 1
            Player.player.current_combo = 1

            boss.generate_vulnerable_spot_coordinates(boss.image, boss_x, boss_y,
                                                      boss_scale)

        if boss.current_hp <= 0:
            Player.player.current_combo = 1

            self.state = 'boss_room_killed'

    def boss_dodged(self):

        global tick_counter

        if tick_counter <= 40:
            show_text('The Boss Dodged', 700, 200, 'red', font_alagard_medium_big)
            show_text('You Got Hit Instead', 700, 240, 'red', font_alagard_medium_big)

        else:
            tick_counter = 0
            if type_of_room == 'mini_boss':
                self.state = 'boss_room'
            else:
                self.state = 'final_boss_fight'
        tick_counter += self.dt * 30

    def boss_room_killed(self):
        global room_counter, tick_counter, active_background

        background()
        frame()

        if tick_counter <= 30:
            show_text('You Killed the Boss!', 150, 120, 'red', font_alagard_big)
        if tick_counter >= 30:
            show_text('Moving Down 1 Floor', 150, 120, 'white', font_alagard_big)

        if tick_counter >= 50:
            Worldinfo.current_dungeon_floor += 1
            Worldinfo.bosses_slayed += 1

            room_counter = 0
            tick_counter = 0
            active_background = main_room

            Player.player.exp += random.randint(150, 200)
            self.state = 'menu'
        tick_counter += self.dt * 30

    def final_boss(self):
        global tick_counter, image_alpha, final_boss, type_of_room, active_background, final_boss_empty_background_button
        active_background = boss_room
        background()

        # Keep In Mind: Red outline when low hp gets hidden because of darkness effect, not sure how to fix
        frame()

        if tick_counter <= 60:
            show_text('THERE IS NO GOING BACK NOW!', 100, 100, 'red', font_alagard_big)
        elif 60 <= tick_counter <= 120:
            image_alpha += 5
            final_boss_image.set_alpha(image_alpha)
            darkness_small_image.set_alpha(image_alpha)
            show_image(final_boss_image, final_boss_x, final_boss_y, 6)
            show_image(darkness_small_image, 0, 0, 7.5)
        else:
            tick_counter = 0
            final_boss = Monster.Boss(10000, True)
            final_boss.generate_vulnerable_spot_coordinates(final_boss_image, final_boss_x, final_boss_y, 6)
            final_boss_empty_background_button = Buttons.Button(empty_background_image, final_boss_x - 95,
                                                                final_boss_y - 60, 13)
            type_of_room = 'final_boss'
            self.state = 'final_boss_fight'

        tick_counter += self.dt * 30

    def final_boss_fight(self):
        global final_boss, image_alpha
        background()
        frame()

        vulnerable_spot_button.rect.x = final_boss.vulnerable_x_coordinate
        vulnerable_spot_button.rect.y = final_boss.vulnerable_y_coordinate
        final_boss_empty_background_button.render_image(screen)

        show_image(final_boss_image, final_boss_x, final_boss_y, 6)
        darkness_small_image.set_alpha(image_alpha)
        show_image(darkness_small_image, 0, 0, 7.5)

        final_boss.draw_health_bar(screen, final_boss_x, final_boss_y - 45)
        vulnerable_spot_button.render_image(screen)

        if vulnerable_spot_button.got_pressed():
            result = random.choice(['dodge', 'hit', 'hit', 'hit', 'hit'])
            if result == 'hit':
                final_boss.current_hp -= Player.player.damage
                # generate new spots
                final_boss.generate_vulnerable_spot_coordinates(final_boss_image, final_boss_x, final_boss_y, 6)
                Player.player.current_combo += 1
                # update the damage stats

            else:
                final_boss.generate_vulnerable_spot_coordinates(final_boss_image, final_boss_x, final_boss_y, 6)
                Player.player.current_hp -= 1
                Player.player.current_combo = 1
                self.state = 'boss_dodged'

        if final_boss_empty_background_button.got_pressed() and not vulnerable_spot_button.mouse_hover():
            Player.player.current_hp -= 1
            Player.player.current_combo = 1

            final_boss.generate_vulnerable_spot_coordinates(final_boss_image, final_boss_x, final_boss_y, 6)

        if final_boss.current_hp <= 0:
            Player.player.current_combo = 1
            Worldinfo.bosses_slayed += 1
            self.state = 'final_boss_killed'

    def final_boss_killed(self):
        background()
        frame()
        final_boss_door_button.render_image(screen)

        if final_boss_door_button.got_pressed():
            self.state = 'victory_room'

    def defeated(self):
        background()
        frame()

        show_text('GAME OVER', 150, 120, 'red', font_alagard_big)
        show_text('STATS:', 150, 180, 'white', font_alagard_big)
        show_text(f'Bosses Slayed: {Worldinfo.bosses_slayed}', 150, 240, 'white', font_alagard_big)
        show_text(f'Monsters Slayed: {Worldinfo.monsters_slayed}', 150, 300, 'white', font_alagard_big)
        show_text(f'Chests Opened: {Worldinfo.chests_opened}', 150, 360, 'white', font_alagard_big)
        show_text(f'Traps Triggered: {Worldinfo.traps_triggered}', 150, 420, 'white', font_alagard_big)

    def victory_room(self):
        global active_background
        active_background = ending_background

        background()
        show_text('YOU WON', 100, 100, 'yellow', font_alagard_huge)
        show_text('STATS:', 550, 280, 'white', font_alagard_big)
        show_text(f'Bosses Slayed: {Worldinfo.bosses_slayed}', 550, 340, 'white', font_alagard_big)
        show_text(f'Monsters Slayed: {Worldinfo.monsters_slayed}', 550, 400, 'white', font_alagard_big)
        show_text(f'Chests Opened: {Worldinfo.chests_opened}', 550, 460, 'white', font_alagard_big)
        show_text(f'Traps Triggered: {Worldinfo.traps_triggered}', 550, 520, 'white', font_alagard_big)

    def state_manager(self, dt):
        global inventory_input
        self.dt = dt
        # all scenes
        if self.state == 'start_game':
            self.start_game()

        if self.state == "tutorial":
            self.tutorial()

        if self.state == "credits":
            self.credits()

        if self.state == 'menu':
            self.menu()

        if self.state == 'menu_with_final_boss':
            self.menu_with_final_boss()

        if self.state == 'monster_room':
            self.monster_room()

        if self.state == 'fight':
            self.fight()

        if self.state == 'monster_room_killed':
            self.monster_room_killed()

        if self.state == 'monster_room_tie':
            self.monster_room_tie()

        if self.state == 'monster_room_loss':
            self.monster_room_loss()

        if self.state == 'chest_room':
            self.chest_room()
        if self.state == 'chest_room_opened':
            self.chest_room_opened()

        if self.state == 'spike_room':
            self.spike_room()

        if self.state == 'mimic_room':
            self.mimic_room()

        if self.state == 'mimic_room_opened':
            self.mimic_room_opened()

        if self.state == 'room_to_boss_room':
            self.room_to_boss_room()

        if self.state == 'boss_room':
            self.boss_room()

        if self.state == 'boss_dodged':
            self.boss_dodged()

        if self.state == 'boss_room_killed':
            self.boss_room_killed()

        if self.state == 'final_boss':
            self.final_boss()

        if self.state == 'final_boss_fight':
            self.final_boss_fight()

        if self.state == 'final_boss_killed':
            self.final_boss_killed()

        if self.state == 'defeated':
            self.defeated()

        if self.state == 'victory_room':
            self.victory_room()

        # things that should be done/checked throughout the entire game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            inventory_input = 0
            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                # inventory slots
                if event.key == pygame.K_1:
                    inventory_input = 1
                if event.key == pygame.K_2:
                    inventory_input = 2
                if event.key == pygame.K_3:
                    inventory_input = 3
                if event.key == pygame.K_4:
                    inventory_input = 4
                if event.key == pygame.K_5:
                    inventory_input = 5
                if event.key == pygame.K_6:
                    inventory_input = 6

                if event.key == pygame.K_e:
                    Player.player.drink_potion()

        exit_button.render_text(screen)
        if exit_button.text_button():
            pygame.quit()
            sys.exit()

        if Player.player.current_hp <= 0:
            self.state = 'defeated'

        Player.player.calculate_damage_multiplier(monster_type)
        Player.player.update_player_stats()

        pygame.display.flip()
