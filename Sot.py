###############################################
#Names: Shane Crawford, Jonathon Dequeant, Dawn Durand
#Date:  4/4/24
#Description: A procedurally generated game similar to Oregon Trail
###############################################

# from pygame import *
import pygame
import sys
import pygame_menu as pm 
from Button import Button

from pygame.locals import (
    KEYDOWN,
    MOUSEBUTTONDOWN,
    QUIT,
    VIDEORESIZE,
    RESIZABLE
)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BG = pygame.image.load("space.jpg")
BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.init()


class Font:
    """
    Function to get a font with a specified size and font name.

    Parameters:
    - font_size: int, size of the font
    - font_name: str, name of the font (default is None)

    Returns:
    - pygame Font object
    """
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.font = pygame.font.Font(None, size)

    def set_size(self, size):
        self.size = size
        self.font = pygame.font.Font(None, size)

    def __repr__(self):
        return f"Font('{self.name}', {self.size})"

    def render_text(self, text, color):
        return self.font.render(text, True, color)


def get_font(font_size, font_name=None):
    
    return pygame.font.Font(font_name, font_size)


def play():
    """
    Function to start the game
    """
    pygame.display.set_caption("Game menu")
    print("play button pressed")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
        screen.fill((255, 255, 255))
        screen.blit(BG, (0, 0))
        MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.078), None).render("This is the game menu screen", True, "white")
        screen.blit(MENU_TEXT, (int(SCREEN_WIDTH * 0.5) - MENU_TEXT.get_width() // 2, int(SCREEN_HEIGHT * 0.25) - MENU_TEXT.get_height() // 2))


        pygame.display.flip()



def options():
    """
    Function to open the options menu
    """
    pygame.display.set_caption("Options")
    print("option button pressed")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
        screen.fill((255, 255, 255))
        screen.blit(BG, (0, 0))
        MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.039), None).render("This is the options screen", True, "White")
        screen.blit(MENU_TEXT, (int(SCREEN_WIDTH * 0.5) - MENU_TEXT.get_width() // 2, int(SCREEN_HEIGHT * 0.25) - MENU_TEXT.get_height() // 2))


        pygame.display.flip()

def main_menu():
    """
    Function to open the main menu.
    """
    pygame.display.set_caption("Menu")
    button_surface = pygame.image.load("button.png")
    button_surface_hover = pygame.image.load("button_hover.png")
    button_surface = pygame.transform.scale(button_surface, (400, 150))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

    running = True

    PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("button.png"), (200, 75)),
                        x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2,
                        text_input="PLAY", font=get_font(50))

    OPTIONS_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("button.png"), (200, 75)),
                        x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + 100,
                        text_input="Options", font=get_font(50))

    QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("button.png"), (200, 75)),
                        x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + 200,
                        text_input="Quit", font=get_font(50))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if PLAY_BUTTON.rect.collidepoint(mouse_pos):
                    play()
                elif OPTIONS_BUTTON.rect.collidepoint(mouse_pos):
                    options()
                elif QUIT_BUTTON.rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        screen.fill((255, 255, 255))
        screen.blit(BG, (0, 0))
        MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.078), None).render("MAIN MENU", True, "White")
        screen.blit(MENU_TEXT, (int(SCREEN_WIDTH * 0.5) - MENU_TEXT.get_width() // 2, int(SCREEN_HEIGHT * 0.25) - MENU_TEXT.get_height() // 2))

        PLAY_BUTTON.update(screen)
        OPTIONS_BUTTON.update(screen)
        QUIT_BUTTON.update(screen)
        PLAY_BUTTON.change_color(pygame.mouse.get_pos())
        OPTIONS_BUTTON.change_color(pygame.mouse.get_pos())
        QUIT_BUTTON.change_color(pygame.mouse.get_pos())

        pygame.display.flip()


    while True:
        screen.fill((255, 255, 255))
        screen.blit(BG, (0, 0))
        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.update(screen)
            button.change_color(pygame.mouse.get_pos())

            if button.checkForInput(pygame.mouse.get_pos()):
                if button.text_input == "PLAY":
                    play()
                elif button.text_input == "Options":
                    options()
                elif button.text_input == "Quit":
                    pygame.quit()
                    sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

main_menu()
