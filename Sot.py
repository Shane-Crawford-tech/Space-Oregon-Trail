###############################################
#Names: Shane Crawford, Jonathon Dequeant, Dawn Durand
#Date:  4/4/24
#Description: A procedurally generated game similar to Oregon Trail
###############################################

#importing libraries
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
    
    button_surface = pygame.image.load("button.png")
    button_surface_hover = pygame.image.load("button_hover.png")
    button_surface = pygame.transform.scale(button_surface, (400, 150))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

    running = True

    EASY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("button.png"), (200, 75)),
                        x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2,
                        text_input="Easy", font=get_font(50))

    NORMAL_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("button.png"), (200, 75)),
                        x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + 100,
                        text_input="Normal", font=get_font(50))

    HARD_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("button.png"), (200, 75)),
                        x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + 200,
                        text_input="Hard", font=get_font(50))

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
                if EASY_BUTTON.rect.collidepoint(mouse_pos):
                    easy(startGame)
                elif NORMAL_BUTTON.rect.collidepoint(mouse_pos):
                    normal(startGame)
                elif HARD_BUTTON.rect.collidepoint(mouse_pos):
                    hard(startGame)

        screen.fill((255, 255, 255))
        BG = pygame.image.load("space.jpg")
        BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(BG, (0, 0))
        MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.078), None).render("Choose your difficulty", True, "White")
        screen.blit(MENU_TEXT, (int(SCREEN_WIDTH * 0.5) - MENU_TEXT.get_width() // 2, int(SCREEN_HEIGHT * 0.25) - MENU_TEXT.get_height() // 2))

        EASY_BUTTON.update(screen)
        NORMAL_BUTTON.update(screen)
        HARD_BUTTON.update(screen)
        EASY_BUTTON.change_color(pygame.mouse.get_pos())
        NORMAL_BUTTON.change_color(pygame.mouse.get_pos())
        HARD_BUTTON.change_color(pygame.mouse.get_pos())

        pygame.display.flip()



def options():
    """
    Function to open the options menu
    """
    global SCREEN_WIDTH, SCREEN_HEIGHT  

    pygame.display.set_caption("Options")

    resolution = [("1280x720", (1280, 720)),
                  ("1600x900", (1600, 900)),
                  ("1920x1080", (1920, 1080)), 
                  ("1920x1200", (1920, 1200)), 
                  ("2560x1440", (2560, 1440)), 
                  ("3840x2160", (3840, 2160))]
    
    # Creates  pygame menu Menu
    settings = pm.Menu(title="Settings",
                       width=SCREEN_WIDTH,
                       height=SCREEN_HEIGHT,
                       theme=pm.themes.THEME_DARK)
    
    # Set default resolution as the initial value for the dropdown
    resolution_dropdown = settings.add.dropselect(title="Window Resolution", items=resolution, 
                                                dropselect_id="Resolution", default=0)  # Set default index to 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    prev_resolution = resolution[0][1]  # Use default resolution as initial previous resolution
    
    event = pygame.event.poll()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if dropdown has been clicked
                if resolution_dropdown.is_selected():
                    current_resolution_index = resolution_dropdown.get_value()[1]  # Get the index of the selected resolution
                    current_resolution = resolution[current_resolution_index][1]  # Get the resolution tuple
                    # Check if resolution has changed
                    if current_resolution != prev_resolution:
                        SCREEN_WIDTH, SCREEN_HEIGHT = current_resolution
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
                        prev_resolution = current_resolution
                        
                        
        settings.update(pygame.event.get())
        screen.fill((255, 255, 255))
        BG = pygame.image.load("space.jpg")
        BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(BG, (0, 0))
        MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.039), None).render("This is the options screen", True, "white")
        screen.blit(MENU_TEXT, (int(SCREEN_WIDTH * 0.5) - MENU_TEXT.get_width() // 2, int(SCREEN_HEIGHT * 0.25) - MENU_TEXT.get_height() // 2))
        settings.draw(screen)
        settings.update([event])
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
        BG = pygame.image.load("space.jpg")
        BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
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
