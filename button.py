import pygame

screen = pygame.display.set_mode((900, 500))

class Button():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.rect = img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw(self):
        action = False
        
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                if self.clicked == False:
                    self.clicked = True
            else:
                if self.clicked:
                    action = True
                self.clicked = False
                    
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                
        screen.blit(self.img, (self.x, self.y))
        
        return action