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
    test_text = font.render(text, True, (color))
    screen.blit(test_text, (x, y))

def random_item():
    # randomize stats for items
    # makes copy
    random_items_list = copy.deepcopy((random.choice(random.choice(Items.items_list)), random.choice(random.choice(Items.items_list)), random.choice(random.choice(Items.items_list))))
    for item in random_items_list:

        if item.type == 'weapon':
            item.strength = random.randint(3, 13) * Worldinfo.current_dungeon_floor

        if item.type == 'armour':
            item.defence = random.randint(3, 13) * Worldinfo.current_dungeon_floor

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



def frame():
    global selected_weapon_frame_x
    global selected_armour_frame_x
    global selected_potion_frame_x


    screen.blit(frame_image, (0, 0))

    # displayed stats:
    show_text(f"HP: {Player.player.current_hp}/ {Player.player.hp}", 1020, 2, "white", font_alagard_small)
    show_text(f"STR: {int(Player.player.damage/Player.player.current_combo)} x {Player.player.current_combo}", 1020, 15, "white", font_alagard_small)
    show_text(f"DEF: {Player.player.total_defence}", 1020, 28, "white", font_alagard_small)
    show_text(f'Player level: {Player.player.lvl}', 546, 10, 'white', font_alagard_medium)
    show_text(f'Dungeon floor: {Worldinfo.current_dungeon_floor}', 546, 30, 'white', font_alagard_medium)

    # weapon icons
    if not Player.player.weapon_inventory[0] == 'Empty':
        show_image(Player.player.weapon_inventory[0].icon, 45, -4, 4)
    if not Player.player.weapon_inventory[1] == 'Empty':
        show_image(Player.player.weapon_inventory[1].icon, 113, -4, 4)

    # empty weapon
    if empty_inv_button1.got_pressed():
        selected_weapon_frame_x = 37.5
        Player.player.equipped_weapon = 0
        Player.player.update_player_stats()
    elif empty_inv_button2.got_pressed():
        selected_weapon_frame_x = 105
        Player.player.equipped_weapon = 1
        Player.player.update_player_stats()
    show_image(gold_frame_image, selected_weapon_frame_x, 0, 7.5)

    # armour icons
    if not Player.player.armour_inventory[0] == 'Empty':
        show_image(Player.player.armour_inventory[0].icon, 215, 0, 4)
    if not Player.player.armour_inventory[1] == 'Empty':
        show_image(Player.player.armour_inventory[1].icon, 283, 0, 4)

    # empty armour
    if empty_inv_button3.got_pressed():
        selected_armour_frame_x = 210
        Player.player.equipped_armour = 0
        Player.player.update_player_stats()
    elif empty_inv_button4.got_pressed():
        selected_armour_frame_x = 278
        Player.player.equipped_armour = 1
        Player.player.update_player_stats()
    show_image(gold_frame_image, selected_armour_frame_x, 0, 7.5)

    # potion icon
    if not Player.player.potion_inventory[0] == 'Empty':
        show_image(Player.player.potion_inventory[0].icon, 390, -4, 4)
    if not Player.player.potion_inventory[1] == 'Empty':
        show_image(Player.player.potion_inventory[1].icon, 458, -4, 4)

    # empty potion
    if empty_inv_button5.got_pressed():
        selected_potion_frame_x = 383
        Player.player.equipped_potion = 0
    elif empty_inv_button6.got_pressed():
        selected_potion_frame_x = 451
        Player.player.equipped_potion = 1
    show_image(gold_frame_image, selected_potion_frame_x, 0, 7.5)

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

    # check for key inputs related to inventory items
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_e:
                # drink potion
                Player.player.drink_potion()



# initiates pygame
pygame.init()

# Screen
width = 1200
height = 675
screen = pygame.display.set_mode((width, height))


# Fonts
font_alagard_big = pygame.font.Font("Fonts/alagard.ttf", 70)
font_alagard_small = pygame.font.Font("Fonts/alagard.ttf", 15)
font_alagard_medium = pygame.font.Font('Fonts/alagard.ttf', 25)

# backgrounds
main_menu_background = pygame.image.load("Images/Start bild.png")
main_menu_background = pygame.transform.scale(main_menu_background, (width, height))

main_room = pygame.image.load('Images/main room.png')
main_room = pygame.transform.scale(main_room, (width, height))

boss_room = pygame.image.load('Images/Boss_room.png')
boss_room = pygame.transform.scale(boss_room, (width, height))

active_background = main_menu_background

frame_image = pygame.image.load('Images/Frame.png')
frame_image = pygame.transform.scale(frame_image, (width, height))

# images
small_chest = pygame.image.load("Images/Chest.png")
inventory_image = pygame.image.load('Images/Inventory_slot.png')
door_image = pygame.image.load('Images/Door.png')
hole_image = pygame.image.load('Images/Hole.png')
spike_image = pygame.image.load('Images/spike_trap.png')
gold_frame_image = pygame.image.load("Images/GoldFrame.png")
open_chest_image = pygame.image.load("Images/open_chest.png")
chest_item_frame_image = pygame.image.load("Images/chest_loot_frame.png")
green_progress = pygame.image.load("Images/green.png")
empty_inv_image = pygame.image.load('Images/empty_inv.png')
torch_image = pygame.image.load('Images/torch.png')

zombie_image = pygame.image.load('Images/zombie.png')
spider_image = pygame.image.load('Images/spindel_prot.png')
zombie_boss_image = pygame.image.load('Images/zombie_boss.png')
zombie_boss_image_2 = pygame.image.load('Images/zombie_boss_2.png')

# empty background image
empty_background_image = pygame.image.load('Images/empty_background.png')


# making button images
inventory_button = Buttons.Button(inventory_image, 0, 0, 0.3)
door_button_1 = Buttons.Button(door_image, 100, 190, 6)
door_button_2 = Buttons.Button(door_image, 500, 190, 6)
door_button_3 = Buttons.Button(door_image, 900, 190, 6)
small_chest_button = Buttons.Button(small_chest, 565, 450, 6)
door_button_chest_room = Buttons.Button(door_image, 150, 190, 6)
door_button_monster_room = Buttons.Button(door_image, 600, 190, 6)
door_to_boss = Buttons.Button(door_image, 500, 190, 6)


# monster buttons
# x och y ändras i gamestate
spider_button = Buttons.Button(spider_image, 0, 0, 3)
zombie_button = Buttons.Button(zombie_image, 0, 0, 5)

zombie_boss_scale = 6
zombie_boss_x = 450
zombie_boss_y = 220
zombie_boss_button = Buttons.Button(zombie_boss_image, zombie_boss_x, zombie_boss_y, zombie_boss_scale)

# vulnerable spot image
vulnerable_spot_image = pygame.image.load('Images/vulnerable_spot.png')

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
exit_button = TextButtons.TextButton(width - 100, 60, 'X', 'red', 'Fonts/alagard.ttf')
new_game_button = TextButtons.TextButton(200, 200, 'New game', 'white', 'Fonts/alagard.ttf')




# variables

monster_type = None
room_type = None


tick_counter = 0
room_counter = 0

selected_weapon_frame_x = 37.5
selected_armour_frame_x = 210
selected_potion_frame_x = 383

clock = pygame.time.Clock()


class GameState():
    def __init__(self):
        self.state = 'start_game'


    def start_game(self):
        global active_background

        background()
        new_game_button.render_text(screen)
        if new_game_button.text_button():
            active_background = main_room
            self.state = 'menu'


    def menu(self):
        global room_type, room_counter, monster, monster_type, monster_x, monster_y

        background()
        frame()

        door_button_1.render_image(screen)
        door_button_2.render_image(screen)
        door_button_3.render_image(screen)

        if door_button_1.got_pressed() or door_button_2.got_pressed() or door_button_3.got_pressed():
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



    def trap_room(self):
        global room_counter, tick_counter, room_type

        background()
        frame()


        if tick_counter <= 20:
            show_text("It's a Dead End", 150, 120, 'white', font_alagard_big)
        if tick_counter >= 25:
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

        tick_counter += 1



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
            Player.player.update_player_stats()

            self.state = 'menu'

        item2_chest_button.render_image(screen)
        if item2_chest_button.got_pressed():
            Player.player.add_item_to_inventory(random_items[1])
            room_counter += 1
            Player.player.update_player_stats()

            self.state = 'menu'

        item3_chest_button.render_image(screen)
        if item3_chest_button.got_pressed():
            Player.player.add_item_to_inventory(random_items[2])
            room_counter += 1
            Player.player.update_player_stats()

            self.state = 'menu'


    def monster_room(self):
        global room_counter

        background()
        frame()

        door_button_monster_room.render_image(screen)

        if door_button_monster_room.got_pressed():
            room_counter += 1
            self.state = 'menu'
        #print(Player.player.strength, monster.strength)

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

    def fight(self):
        if Player.player.damage > monster.strength:
            self.state = 'monster_room_killed'

        elif Player.player.damage == monster.strength:
            self.state = 'monster_room_tie'

        else:
            Player.player.current_hp -= 1
            self.state = 'monster_room_loss'

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
        global active_background, boss, vulnerable_spot_x, vulnerable_spot_y, empty_background_button
        background()
        frame()


        door_to_boss.render_image(screen)
        show_text('YOU FOUND THE BOSS', 150, 120, 'red', font_alagard_big)
        show_image(torch_image, 420, 240, 5)
        show_image(torch_image, 740, 240, 5)

        if door_to_boss.got_pressed():
            active_background = boss_room
            # creates the boss object
            boss = Monster.Boss(100, 5)
            if boss.type == 'zombie_boss':
                # generate the first spot
                boss.generate_vulnerable_spot_coordinates(zombie_boss_image, zombie_boss_x, zombie_boss_y, zombie_boss_scale)
                empty_background_button = Buttons.Button(empty_background_image, zombie_boss_x-95, zombie_boss_y-60, 13)

            self.state = 'boss_room'



    def boss_room(self):

        background()
        frame()
        boss.calculate_health_bar_image()
        show_image(boss.current_health_bar_image, zombie_boss_x - 20, zombie_boss_y - 50, 5)
        show_text(f'COMBO: x{Player.player.current_combo}', 100, 120, 'white', font_alagard_big)
        if boss.type == 'zombie_boss':

            zombie_boss_button.render_image(screen)

            empty_background_button.render_image(screen)

            vulnerable_spot_button.rect.x = boss.vulnerable_x_coordinate
            vulnerable_spot_button.rect.y = boss.vulnerable_y_coordinate
            vulnerable_spot_button.render_image(screen)

            if vulnerable_spot_button.got_pressed():
                result = random.choice(['dodge'])
                if result == 'hit':
                    boss.current_hp -= Player.player.damage
                    # generate new spots
                    boss.generate_vulnerable_spot_coordinates(zombie_boss_image, zombie_boss_x, zombie_boss_y, zombie_boss_scale)
                    Player.player.current_combo += 1
                    # update the damage stats
                    Player.player.update_player_stats()
                else:
                    boss.generate_vulnerable_spot_coordinates(zombie_boss_image, zombie_boss_x, zombie_boss_y, zombie_boss_scale)
                    Player.player.current_hp -= 1
                    Player.player.current_combo = 1
                    Player.player.update_player_stats()

                    self.state = 'boss_dodged'


            if empty_background_button.got_pressed() and not vulnerable_spot_button.mouse_hover():
                Player.player.current_hp -= 1
                Player.player.current_combo = 1
                Player.player.update_player_stats()
                boss.generate_vulnerable_spot_coordinates(zombie_boss_image, zombie_boss_x, zombie_boss_y, zombie_boss_scale)

        if boss.current_hp <= 0:
            Player.player.current_combo = 1
            Player.player.update_player_stats()
            self.state = 'boss_room_killed'


    def boss_dodged(self):
        global tick_counter
        print(tick_counter)
        if tick_counter <= 200:
            show_text('The Boss Dodged', 100, 200, 'red', font_alagard_big)
        if tick_counter >= 400:
            show_text('You Got Hit Instead', 100, 200, 'red', font_alagard_big)

        if tick_counter >= 800:
            tick_counter = 0
            self.state = 'boss_room'
        tick_counter += 1

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
            self.state = 'menu'
        tick_counter += 1

    def defeated(self):
        background()
        frame()

        show_text('GAME OVER', 150, 120, 'red', font_alagard_big)
        show_text('STATS:', 150, 180, 'white', font_alagard_big)
        show_text(f'Bosses Slayed: {Worldinfo.bosses_slayed}', 150, 240, 'white', font_alagard_big)
        show_text(f'Monsters Slayed: {Worldinfo.monsters_slayed}', 150, 300, 'white', font_alagard_big)
        show_text(f'Chests Opened: {Worldinfo.chests_opened}', 150, 360, 'white', font_alagard_big)
        show_text(f'Traps Triggered: {Worldinfo.traps_triggered}', 150, 420, 'white', font_alagard_big)


    def state_manager(self):
        # all scenes
        if self.state == 'start_game':
            self.start_game()

        if self.state == 'menu':
            self.menu()

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

        if self.state == 'trap_room':
            self.trap_room()

        if self.state == 'room_to_boss_room':
            self.room_to_boss_room()

        if self.state == 'boss_room':
            self.boss_room()

        if self.state == 'boss_dodged':
            self.boss_dodged()

        if self.state == 'boss_room_killed':
            self.boss_room_killed()

        if self.state == 'defeated':
            self.defeated()


        # things that should be done/checked throughout the entire game
        # could also put this in main
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        exit_button.render_text(screen)
        if exit_button.text_button():
            pygame.quit()
            sys.exit()

        if Player.player.current_hp <= 0:
            self.state = 'defeated'

        pygame.display.flip()
