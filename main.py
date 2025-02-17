import pygame
import sys
import os

screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('Nothing Can Go Wrong, Right?')

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()