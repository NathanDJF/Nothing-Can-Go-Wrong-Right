import pygame
import sys
import os
import random
import string
from button import Button
from timer import Timer
from firstcutscene import Cutscene

# screen
pygame.init()
pygame.mixer.music.load('Assets/audio/main theme.mp3')
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('Nothing Can Go Wrong, Right?')

start_time = None
time_since_robbery = None

# font
font = pygame.font.Font('Assets/font/DynaPuff-VariableFont_wdth,wght.ttf', 36)
font2 = pygame.font.Font('Assets/font/DynaPuff-VariableFont_wdth,wght.ttf', 10)

#deltatime
clock = pygame.time.Clock()

# images
fail_img = pygame.image.load(os.path.join('Assets/images/fail.png'))
money_button_img = pygame.image.load(os.path.join('Assets/images/bribery button.png'))
bribing_button_img = pygame.image.load(os.path.join('Assets/images/bribery button.png'))
programming_job_button_img = pygame.image.load(os.path.join('Assets/images/programming job button.png'))
robbery_job_button_img = pygame.image.load(os.path.join('Assets/images/robbery job button.png'))
gambling_job_button_img = pygame.image.load(os.path.join('Assets/images/gamble job button.png'))
black_button_img = pygame.image.load(os.path.join('Assets/images/black button.png'))
red_button_img = pygame.image.load(os.path.join('Assets/images/red button.png'))
green_button_img = pygame.image.load(os.path.join('Assets/images/green button.png'))
roulette_img = pygame.image.load(os.path.join('Assets/images/roulette.png'))
win_screen_img = pygame.image.load(os.path.join('Assets/images/win screen.png'))

money_button = Button(200, 200, money_button_img)
bribery_button = Button(600, 200, bribing_button_img)
programming_job_button = Button(140, 180, programming_job_button_img)
robbery_job_button = Button(180, 140, robbery_job_button_img)
gambling_job_button = Button(240, 140, gambling_job_button_img)
black_button = Button(325, 400, black_button_img)
red_button = Button(425, 400, red_button_img)
green_button = Button(525, 400, green_button_img)

# variables
money = 0
lose_chance = 0
lose_chance_picked = False
bribe_amount_needed = 5000
visit_grandma = 0
first_cutscene_playing = True
menu_on = False
money_button_menu = False
programming_job_menu = False
robbery_job_menu = False
gambling_job_menu = False
words_picked = False
chosen_words = ''
characters_word_1 = list()
characters_word_2 = list()
characters_word_3 = list()
display_word_1 = True
display_word_2 = True
display_word_3 = True
letter = ' '
rob_chance_picked = False
rob_chance = 11.5
rob_amount_picked = False
robbery_timer = Timer(3000)
programming_timer = Timer(3000)
gambling_timer = Timer(3000)
gambling_chance_picked = False
color_chosen = False
gambling_success = False
gambling_failed = False

# money button + jobs
    
def menu():
    global money
    global menu_on
    global money_button_menu
    global programming_job_menu
    global robbery_job_menu
    global gambling_job_menu
    global lose_chance_picked
    global lose_chance
    global bribe_amount_needed
    global visit_grandma
    
    screen.fill((254, 220, 183))
    money_count = font.render("Money: " + str(money), True, (0, 0, 0))
    
    if money_button.draw():
        money_button_menu = True
        
    if bribery_button.draw():
        if lose_chance_picked == False:
            lose_chance = random.randint(1, 20)
            lose_chance_picked = True
        
        if money >= bribe_amount_needed:
            money -= bribe_amount_needed
            bribe_amount_needed *= 1.5
            visit_grandma += 1
        
        if lose_chance == 10:
            screen.blit(fail_img, (0, 0))
            pygame.mixer.Sound.play(pygame.mixer.Sound('Assets/audio/Losing.mp3'), 0)
            
        if visit_grandma == 5:
            screen.fill((254, 220, 183))
            screen.blit(win_screen_img, (350, 200))
    
    if money_button_menu:
        if programming_job_button.draw():
            money_button_menu = False
            menu_on = False
            programming_job_menu = True
        if robbery_job_button.draw():
            money_button_menu = False
            menu_on = False
            robbery_job_menu = True
        if gambling_job_button.draw():
            money_button_menu = False
            menu_on = False
            gambling_job_menu = True
    
    screen.blit(money_count, (20, 450))
            
# programming job

def programming_job():
    global money
    global words_picked
    global chosen_words
    global characters_word_1, characters_word_2, characters_word_3
    global display_word_1, display_word_2, display_word_3
    global programming_job_menu
    global programming_timer
    global menu_on
    
    list_of_words = ["print", "for", "if", "wrong", "variable", "blit", "def", "class", "struct", "while"]
    screen.fill((254, 220, 183))

    
    if words_picked == False:
        chosen_words = random.sample(list_of_words, 3)
        characters_word_1 = list(chosen_words[0])
        characters_word_2 = list(chosen_words[1])
        characters_word_3 = list(chosen_words[2])

        words_picked = True
    
    word_1_display = font.render(chosen_words[0], True, (0, 0, 0))
    word_2_display = font.render(chosen_words[1], True, (0, 0, 0))
    word_3_display = font.render(chosen_words[2], True, (0, 0, 0))
    if display_word_1:
        screen.blit(word_1_display, (50, 30))
    if display_word_2:
        screen.blit(word_2_display, (50, 80))
    if display_word_3:
        screen.blit(word_3_display, (50, 130))
    
    keys = pygame.key.get_pressed()
    
    for letter in string.ascii_lowercase:
        key = getattr(pygame, f'K_{letter}')
        if keys[key]:
            if letter in characters_word_1:
                characters_word_1.remove(letter)
                if len(characters_word_1) == 0:
                    display_word_1 = False
                    
            if letter in characters_word_2:
                characters_word_2.remove(letter)
                if len(characters_word_2) == 0:
                    display_word_2 = False
                    
            if letter in characters_word_3:
                characters_word_3.remove(letter)
                if len(characters_word_3) == 0:
                    display_word_3 = False
    
    if (len(characters_word_1) == 0) and (len(characters_word_2) == 0) and (len(characters_word_3) == 0):
        if not programming_timer.active:
            programming_timer.activate()
            
        screen.fill((254, 220, 183))
        success_text = font.render("Success!", True, (0, 0, 0))
        program_amount_text = font.render("Earned $" + str(5000), True, (0, 0, 0))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Assets/audio/Winning.mp3'), 0)
        
        screen.blit(success_text, (390, 150))
        screen.blit(program_amount_text, (350, 200))
        programming_timer.update()
        
        if not programming_timer.active:
            screen.fill((254, 220, 183))
            money += 5000
            programming_job_menu = False
            words_picked = False
            display_word_1 = True
            display_word_2 = True
            display_word_3 = True
            menu_on = True
        
def robbery_job():
    global money
    global rob_chance_picked
    global rob_chance
    global rob_amount_picked
    global rob_amount
    global robbery_job_menu
    global robbery_timer
    global menu_on
    screen.fill((254, 220, 183))
    
    if not robbery_timer.active:
        robbery_timer.activate()
    
    if rob_chance_picked == False:
        rob_chance = random.randint(1, 25)
        rob_chance_picked = True
      
    if rob_chance_picked:
          
        if rob_chance >= 12:
            if rob_amount_picked == False:
                rob_amount = random.randint(10, 50000)
                money += rob_amount
                rob_amount_picked = True
            
            if rob_amount_picked:
                success_text = font.render("Success!", True, (0, 0, 0))
                rob_amount_text = font.render("Earned $" + str(rob_amount), True, (0, 0, 0))
                pygame.mixer.Sound.play(pygame.mixer.Sound('Assets/audio/Winning.mp3'))
                
                screen.blit(success_text, (390, 150))
                screen.blit(rob_amount_text, (350, 200))
                robbery_timer.update()
                
                if not robbery_timer.active:
                    screen.fill((254, 220, 183))
                    rob_chance = 0
                    rob_amount = 0
                    rob_chance_picked = False
                    rob_amount_picked = False
                    robbery_job_menu = False
                    menu_on = True
            
        elif rob_chance <= 11:
            screen.blit(fail_img, (0, 0))
            pygame.mixer.Sound.play(pygame.mixer.Sound('Assets/audio/Losing.mp3'), 0)
    
def gambling_job():
    global gambling_job_menu
    global menu_on
    global gambling_chance_picked
    global gambling_timer
    global choice
    global color_chosen
    global chosen_color
    global gambling_success
    global gambling_failed
    
    screen.fill((254, 220, 183))
    screen.blit(roulette_img, (300, 50))

    if not gambling_timer.active:
        gambling_timer.activate()
    
    if gambling_chance_picked == False:
        choice = random.randint(1, 101)
        gambling_chance_picked = True
    
    if black_button.draw():
        chosen_color = "black"
        color_chosen = True
    if red_button.draw():
        chosen_color = "red"
        color_chosen = True
    if green_button.draw():
        chosen_color = "green"
        color_chosen = True

    if color_chosen:
        if chosen_color == "black":
            if choice >= 50 and choice < 101:
                gambling_success = True
            else:
                gambling_failed = True
                
        if chosen_color == "red":
            if choice < 50:
                gambling_success = True
            else:
                gambling_failed = True
                
        if chosen_color == "green":
            if choice == 101:
                gambling_success = True
            else:
                gambling_failed = True
    
    if gambling_success:
        
        if not gambling_timer.active:
            gambling_timer.activate()

        screen.fill((254, 220, 183))
        success_text = font.render("Success!", True, (0, 0, 0))
        gamble_amount_text = font.render("Earned $" + str(15000), True, (0, 0, 0))
        pygame.mixer.Sound.play(pygame.mixer.Sound('Assets/audio/Winning.mp3'))
        gambling_timer.update()
        
        screen.blit(success_text, (390, 150))
        screen.blit(gamble_amount_text, (320, 200))
        if not gambling_timer.active:
            gambling_job_menu = False
            menu_on = True
            gambling_chance_picked = False
            choice = 0
            color_chosen = False
            chosen_color = None
            gambling_success = False
            gambling_failed = False
        
    if gambling_failed:
        
        if not gambling_timer.active:
            gambling_timer.activate()
        
        screen.fill((254, 220, 183))
        failed_text = font.render("Failed!", True, (0, 0, 0))
        correct_color = font.render("Correct Color:", True, (0, 0, 0))
        
        screen.blit(failed_text, (390, 100))
        screen.blit(correct_color, (310, 150))
        if choice >= 50 and choice < 101:
            screen.blit(black_button_img, (430, 220))
        if choice < 50:
            screen.blit(red_button_img, (420, 220))
        if choice == 101:
            screen.blit(green_button_img, (420, 220))
        gambling_timer.update()

        if not gambling_timer.active:
            gambling_job_menu = False
            menu_on = True
            gambling_chance_picked = False
            choice = 0
            color_chosen = False
            chosen_color = None
            gambling_success = False
            gambling_failed = False

while True:
    
    clock.tick(12)
    
    if first_cutscene_playing:
        Cutscene.run()
        skip = font2.render("Click to skip", True, (0, 0, 0))
        screen.blit(skip, (10, 10))
        
        if pygame.mouse.get_pressed()[0]:
            first_cutscene_playing = False
            menu_on = True
    
    if menu_on:
        menu()
    
    if programming_job_menu:
        programming_job()
    
    if robbery_job_menu:
        robbery_job()
    
    if gambling_job_menu:
        gambling_job()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    