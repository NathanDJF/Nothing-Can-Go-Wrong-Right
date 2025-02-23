import pygame, os
import sys
from timer import Timer

screen = pygame.display.set_mode((900, 500))
clock = pygame.time.Clock()
frame_counter = 0

f1 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/1.png'))
f2 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/2.png'))
f3 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/3.png'))
f4 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/4.png'))
f5 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/5.png'))
f6 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/6.png'))
f7 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/7.png'))
f8 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/8.png'))
f9 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/9.png'))
f10 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/10.png'))
f11 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/11.png'))
f12 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/12.png'))
f13 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/13.png'))
f14 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/14.png'))
f15 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/15.png'))
f16 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/16.png'))
f17 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/17.png'))
f18 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/18.png'))
f19 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/19.png'))
f20 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/20.png'))
f21 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/21.png'))
f22 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/22.png'))
f23 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/23.png'))
f24 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/24.png'))
f25 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/25.png'))
f26 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/26.png'))
f27 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/27.png'))
f28 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/28.png'))
f29 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/29.png'))
f30 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/30.png'))
f31 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/31.png'))
f32 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/32.png'))
f33 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/33.png'))
f34 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/34.png'))
f35 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/35.png'))
f36 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/36.png'))
f37 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/37.png'))
f38 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/38.png'))
f39 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/39.png'))
f40 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/40.png'))
f41 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/41.png'))
f42 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/42.png'))
f43 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/43.png'))
f44 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/44.png'))
f45 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/45.png'))
f46 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/46.png'))
f47 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/47.png'))
f48 = pygame.image.load(os.path.join('Assets/image collections/first cutscene/48.png'))

frames_list = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11, f12, f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28,f29,f30,f31,
               f32,f33,f34,f35,f36,f37,f38,f39,f40,f41,f42,f43,f44,f45,f46,f47,f48]

clock.tick(12)

class Cutscene:
    def run():
        global first_cutscene_playing
        global menu_on
        global frame_counter
        
        if frame_counter != 47:
            frame_counter += 1
                   
        frame = frames_list[frame_counter]
            
        screen.blit(frame, (0, 0))
        
        if frame_counter == 47:
            menu_on = True
            first_cutscene_playing = False