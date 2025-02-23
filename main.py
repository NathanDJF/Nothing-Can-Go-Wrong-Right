import pygame
import sys
import os
import random
import string
import time
from button import Button
from timer import Timer

# screen
pygame.init()

screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('Nothing Can Go Wrong, Right?')

start_time = None
time_since_robbery = None

# font
font = pygame.font.SysFont('Arial', 36)

# images
fail_img = pygame.image.load(os.path.join('Assets/images/fail.png'))
money_button_img = pygame.image.load(os.path.join('Assets/images/money button placeholder.png'))
programming_job_button_img = pygame.image.load(os.path.join('Assets/images/programming job button placeholder.png'))
robbery_job_button_img = pygame.image.load(os.path.join('Assets/images/robbery job button placeholder.png'))

money_button = Button(200, 200, money_button_img)
programming_job_button = Button(140, 180, programming_job_button_img)
robbery_job_button = Button(180, 140, robbery_job_button_img)

# variables
menu_on = True
money_button_menu = False
selection = False
programming_job_menu = False
robbery_job_menu = False
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

# money button + jobs
    
def menu():
    global menu_on
    global money_button_menu
    global selection
    global programming_job_menu
    global robbery_job_menu
    
    if money_button.draw():
        money_button_menu = True
    
    if money_button_menu:
        selection = True
        if programming_job_button.draw():
            money_button_menu = False
            menu_on = False
            programming_job_menu = True
        if robbery_job_button.draw():
            money_button_menu = False
            menu_on = False
            robbery_job_menu = True
            
# programming job

def programming_job():
    global words_picked
    global chosen_words
    global characters_word_1, characters_word_2, characters_word_3
    global display_word_1, display_word_2, display_word_3
    global last_letter
    global programming_job_menu
    global menu_on
    
    list_of_words = ["print", "for", "if", "wrong", "variable", "blit", "def", "class", "struct", "while"]
    screen.fill((255, 255, 255))
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
    last_letter_text = font.render("Last letter: ", True, (0, 0, 0))
    
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
                    
        last_letter = font.render(letter, True, (0, 0, 0))
    screen.blit(last_letter_text, (50, 200))
    screen.blit(last_letter, (200, 200))
    
    if (len(characters_word_1) == 0) and (len(characters_word_2) == 0) and (len(characters_word_3) == 0):
        screen.fill((255, 255, 255))
        programming_job_menu = False
        words_picked = False
        display_word_1 = True
        display_word_2 = True
        display_word_3 = True
        menu_on = True
        
def robbery_job():
    global rob_chance_picked
    global rob_chance
    global rob_amount_picked
    global rob_amount
    global robbery_job_menu
    global robbery_timer
    global menu_on
    screen.fill((255, 255, 255))
    robbery_timer = Timer(3000)
    robbery_timer.activate()
    if rob_chance_picked == False:
        rob_chance = random.randint(1, 25)
        rob_chance_picked = True
      
    if rob_chance_picked:
          
        if rob_chance >= 12:
            if rob_amount_picked == False:
                rob_amount = random.randint(10, 50000)
                rob_amount_picked = True
            
            if rob_amount_picked:
                success_text = font.render("Success!", True, (0, 0, 0))
                rob_amount_text = font.render("Earned $" + str(rob_amount), True, (0, 0, 0))
                
                screen.blit(success_text, (400, 150))
                screen.blit(rob_amount_text, (350, 200))
                robbery_timer.update()
                
                if not robbery_timer.active:
                    screen.fill((255, 255, 255))
                    rob_chance = 0
                    rob_amount = 0
                    rob_chance_picked = False
                    rob_amount_picked = False
                    robbery_job_menu = False
                    menu_on = True
            
        elif rob_chance <= 11:
            screen.blit(fail_img, (0, 0))
    
clock = pygame.time.Clock()

while True:
    
    clock.tick(60)
    
    if selection == False:
        screen.fill((255, 255, 255))
    
    if menu_on:
        menu()
    
    if programming_job_menu:
        programming_job()
    
    if robbery_job_menu:
        robbery_job()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()