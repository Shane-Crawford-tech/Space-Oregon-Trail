###############################################
#Names: Shane Crawford, Jonathon Dequeant, Dawn Durand
#Date:  4/4/24
#Description: A procedurally generated game similar to Oregon Trail
###############################################

#importing libraries
import pygame
import sys
from Constants import *
import pygame_menu as pm 
from Button import *
from Armor_Health_and_Move_Systems import *
from battles import *
from map_module import run_map
from random import randint
from pygame.locals import (
    KEYDOWN,
    MOUSEBUTTONDOWN,
    QUIT,
    VIDEORESIZE,
    RESIZABLE
)


pygame.init()


def play():
    """
    Function to start the game
    """

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

    running = True

    EASY_BUTTON = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/5, SCREEN_HEIGHT/10)),
                        x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2,
                        text_input="Easy", font=get_font(50))

    NORMAL_BUTTON = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/5, SCREEN_HEIGHT/10)),
                        x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + SCREEN_HEIGHT/8,
                        text_input="Normal", font=get_font(50))

    HARD_BUTTON = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/5, SCREEN_HEIGHT/10)),
                        x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + SCREEN_HEIGHT/4,
                        text_input="Hard", font=get_font(50))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if EASY_BUTTON.rect.collidepoint(mouse_pos):
                    print("you selected easy")
                    run_map(SCREEN_WIDTH, SCREEN_HEIGHT) # As a placeholder for starting the game
                elif NORMAL_BUTTON.rect.collidepoint(mouse_pos):
                    print("you selected normal")
                    run_map(SCREEN_WIDTH, SCREEN_HEIGHT) # As a placeholder for starting the game
                elif HARD_BUTTON.rect.collidepoint(mouse_pos):
                    print("you selected hard")
                    run_map(SCREEN_WIDTH, SCREEN_HEIGHT) # As a placeholder for starting the game
        screen.fill((255, 255, 255))
        BG = pygame.image.load("images\\space.jpg")
        BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(BG, (0, 0))
        MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.078), None).render("Choose your difficulty", True, "White")
        screen.blit(MENU_TEXT, (int(SCREEN_WIDTH * 0.5) - MENU_TEXT.get_width() // 2, int(SCREEN_HEIGHT * 0.25) - MENU_TEXT.get_height() // 2))

        EASY_BUTTON.update(screen)
        NORMAL_BUTTON.update(screen)
        HARD_BUTTON.update(screen)
        #EASY_BUTTON.change_color(pygame.mouse.get_pos())
        #NORMAL_BUTTON.change_color(pygame.mouse.get_pos())
        #HARD_BUTTON.change_color(pygame.mouse.get_pos())

        pygame.display.flip()

def load_config():
    try:
        with open(CONFIG_FILE, "r") as file:
            resolution_index = int(file.read())
            return resolution_index
    except FileNotFoundError:
        return 0  # Default resolution index

def save_config(index):
    with open(CONFIG_FILE, "w") as file:
        file.write(str(index))

def options():
    """
    Function to open the options menu
    """
    global SCREEN_WIDTH, SCREEN_HEIGHT

    pygame.display.set_caption("Options")

    
    default_resolution_index = load_config()
    
    # Creates  pygame menu Menu
    settings = pm.Menu(title="Settings",
                       width=SCREEN_WIDTH,
                       height=SCREEN_HEIGHT,
                       theme=pm.themes.THEME_DARK)
    
    # Set default resolution as the initial value for the dropdown
    resolution_dropdown = settings.add.dropselect(title="Window Resolution", items=resolution, 
                                dropselect_id="Resolution", default=default_resolution_index)  # Set default index to previous resolution or 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    prev_resolution = resolution[default_resolution_index][1]  # Use default resolution as initial previous resolution
    
    event = pygame.event.poll()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_config(resolution_dropdown.get_value()[1])  # Save selected resolution index
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


            screen.fill((255, 255, 255))
            BG = pygame.image.load("images\\space.jpg")
            BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
            screen.blit(BG, (0, 0))
            MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.039), None).render("This is the options screen", True, "white")
            screen.blit(MENU_TEXT, (int(SCREEN_WIDTH * 0.5) - MENU_TEXT.get_width() // 2, int(SCREEN_HEIGHT * 0.25) - MENU_TEXT.get_height() // 2))
        settings.draw(screen)
        settings.update([event])
        pygame.display.flip()

    save_config(resolution_dropdown.get_value()[1])  # Save selected resolution index before exiting options menu


def main_menu():
    """
    Function to open the main menu.
    """
    pygame.display.set_caption("Menu")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

    running = True

    PLAY_BUTTON = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/5, SCREEN_HEIGHT/10)),
                        x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2,
                        text_input="PLAY", font=get_font(50))

    OPTIONS_BUTTON = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/5, SCREEN_HEIGHT/10)),
                        x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + SCREEN_HEIGHT/8,
                        text_input="Options", font=get_font(50))

    QUIT_BUTTON = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/5, SCREEN_HEIGHT/10)),
                        x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + SCREEN_HEIGHT/4,
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
        BG = pygame.image.load("images\\space.jpg")
        BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(BG, (0, 0))
        MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.078), None).render("Space Oregon Trail", True, "White")
        screen.blit(MENU_TEXT, (int(SCREEN_WIDTH * 0.5) - MENU_TEXT.get_width() // 2, int(SCREEN_HEIGHT * 0.25) - MENU_TEXT.get_height() // 2))

        PLAY_BUTTON.update(screen)
        OPTIONS_BUTTON.update(screen)
        QUIT_BUTTON.update(screen)
        #PLAY_BUTTON.change_color(pygame.mouse.get_pos())
        #OPTIONS_BUTTON.change_color(pygame.mouse.get_pos())
        #QUIT_BUTTON.change_color(pygame.mouse.get_pos())
        

        pygame.display.flip()


    while True:
        screen.fill((255, 255, 255))
        screen.blit(BG, (0, 0))
        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.update(screen)
            #button.change_color(pygame.mouse.get_pos())

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


def Inventory_Menu():

    pygame.display.set_caption("Inventory")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    Inventory_Slot = pygame.image.load("images\\inventory slot.png")
    Inventory_Slot = pygame.transform.scale(Inventory_Slot, (SCREEN_HEIGHT//12, SCREEN_HEIGHT//12))
    Inventory_Slot_Size = SCREEN_HEIGHT/12
    
    for column in range(5):
        for row in range(5):
            screen.blit((Inventory_Slot), (row * Inventory_Slot_Size, column * Inventory_Slot_Size))
            screen.fill((255, 255, 255))
    
    runnung = True
    while runnung:
        BG = pygame.image.load("images\\space.jpg")
        BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(BG, (0, 0))

        pygame.display.flip()

# Inventory_Menu()
