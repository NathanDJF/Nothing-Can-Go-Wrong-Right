import pygame
import sys
import os
from button import Button

# screen
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('Nothing Can Go Wrong, Right?')

# images
money_button_img = pygame.image.load(os.path.join('Assets/images/money button placeholder.png'))
programming_job_button_img = pygame.image.load(os.path.join('Assets/images/programming job button placeholder.png'))

money_button = Button(200, 200, money_button_img)
programming_job_button = Button(140, 180, programming_job_button_img)

money_button_menu = False
def money_button_func():
    global money_button_menu
    
    if money_button.draw():
        money_button_menu = True
    
    if money_button_menu:
        if programming_job_button.draw():
            print("hi")
            money_button_menu = False
            
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    screen.fill('white')
    money_button_func()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()