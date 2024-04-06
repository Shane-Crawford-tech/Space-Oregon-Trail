###############################################
#Names: Shane Crawford, Jonathon Dequeant, Dawn Durand
#Date:  4/4/24
#Description: A procedurally generated game similar to Oregon Trail
###############################################

# from pygame import *
import pygame
import sys

from pygame.locals import (
    KEYDOWN,
    MOUSEBUTTONDOWN,
    QUIT,
    VIDEORESIZE,
    RESIZABLE
)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
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
    print("play button pressed")


def options():
    """
    Function to open the options menu
    """
    print("option button pressed")



def main_menu():
    """
    Function to open the main menu.
    """
    pygame.display.set_caption("Menu")


class Button():
    def __init__(self, image, x_pos, y_pos, text_input, font):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.font = font  # Use the provided font object
        self.text = self.font.render(self.text_input, True, (255, 255, 255))  # Use font object to render text
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.clicked = False  # Flag to track if button is clicked

    def update(self, screen):
        """
        Update the button on the screen.

        Parameters:
        - screen: pygame.Surface, the screen surface to blit the button onto
        """
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position, event=None):
        """
        Check for input on the button.

        Parameters:
        - position: tuple, the position of the mouse cursor
        - event: pygame.Event, the event object (default is None)

        Returns:
        - bool, True if the button is clicked, False otherwise
        """
        if event and event.type == MOUSEBUTTONDOWN and event.button == 1:  # Check if left mouse button is clicked
            if self.rect.collidepoint(position):
                self.clicked = True  # Set clicked flag to True when button is clicked
                return True  # Return True when button is clicked
        return False  # Return False otherwise

    def change_color(self, position):
        """
        Change the color of the button text.

        Parameters:
        - position: tuple, the position of the mouse cursor
        """
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, (0, 255, 0))
        else:
            self.text = self.font.render(self.text_input, True, (255, 255, 255))


button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == VIDEORESIZE:
                SCREEN_WIDTH, SCREEN_HEIGHT = event.dict['size']
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)

        elif event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if PLAY_BUTTON.checkForInput(pygame.mouse.get_pos(), event):
                    play()
                elif OPTIONS_BUTTON.checkForInput(pygame.mouse.get_pos(), event):
                    options()
                elif QUIT_BUTTON.checkForInput(pygame.mouse.get_pos(), event):
                    pygame.quit()
                    sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(BG, (0, 0))
    MENU_TEXT = get_font(100).render("MAIN MENU", True, (182, 143, 64))
    screen.blit(MENU_TEXT, (SCREEN_WIDTH // 2 - MENU_TEXT.get_width() // 2, SCREEN_HEIGHT // 4 - MENU_TEXT.get_height() // 2))

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

        pygame.display.flip()

main_menu()