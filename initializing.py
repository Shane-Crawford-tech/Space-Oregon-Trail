#import _.py
import random
import pygame
import sys
import pygame_menu as pm 
from Button import Button
from SOT import *
import Encounters


main_menu()


class startGame():
    def __init__():
        pass
        
    pygame.display.set_caption("SOT")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill((255, 255, 255))
        BG = pygame.image.load("space.jpg")
        BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(BG, (0, 0))
        MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.078), None).render("Start Screen", True, "White")
        screen.blit(MENU_TEXT, (int(SCREEN_WIDTH * 0.5) - MENU_TEXT.get_width() // 2, int(SCREEN_HEIGHT * 0.25) - MENU_TEXT.get_height() // 2))
    pass

class easy(startGame):
    def __init__():
        pass

class normal(startGame):
    def __init__():
        pass

class hard(startGame):
    def __init__():
        pass
