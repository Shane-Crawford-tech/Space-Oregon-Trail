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
from map_module import run_map
from Encounters import *

from pygame.locals import (
    KEYDOWN,
    MOUSEBUTTONDOWN,
    QUIT,
    VIDEORESIZE,
    RESIZABLE
)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CONFIG_FILE = "config.txt"
BUTTON = pygame.image.load("images\\button.png")

resolution = [("1280x720", (1280, 720)),
                ("1600x900", (1600, 900)),
                ("1920x1080", (1920, 1080)), 
                ("1920x1200", (1920, 1200)), 
                ("2560x1440", (2560, 1440)), 
                ("3840x2160", (3840, 2160))]

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
    encounter_button = settings.add.button(title="Encounter Testing")
    
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
                if encounter_button.is_selected():
                    encounter_menu()

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




def encounter_menu():
    """
    Function to display an encounter
    """
                
    pygame.display.set_caption("Encounter")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

    
    #event = pygame.event.poll()
    running = True
    
    if chosen_encounter.number_of_options == 1:
      BUTTON_ONE = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2,
                          text_input=chosen_encounter.encounter_option_list[0], font=get_font(25))

    elif chosen_encounter.number_of_options == 2:
      BUTTON_ONE = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2,
                          text_input=chosen_encounter.encounter_option_list[0], font=get_font(25))
      BUTTON_TWO = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + 50,
                          text_input=chosen_encounter.encounter_option_list[1], font=get_font(25))

    elif chosen_encounter.number_of_options == 3:
      BUTTON_ONE = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2,
                          text_input=chosen_encounter.encounter_option_list[0], font=get_font(25))
      BUTTON_TWO = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + 50,
                          text_input=chosen_encounter.encounter_option_list[1], font=get_font(25))
      BUTTON_THREE = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + 100,
                          text_input=chosen_encounter.encounter_option_list[2], font=get_font(25))
      
    elif chosen_encounter.number_of_options == 4:
      BUTTON_ONE = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2,
                          text_input=chosen_encounter.encounter_option_list[0], font=get_font(25))
      BUTTON_TWO = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + 50,
                          text_input=chosen_encounter.encounter_option_list[1], font=get_font(25))
      BUTTON_THREE = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + 100,
                          text_input=chosen_encounter.encounter_option_list[2], font=get_font(25))
      BUTTON_FOUR = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + 150,
                          text_input=chosen_encounter.encounter_option_list[3], font=get_font(25))
      
    elif chosen_encounter.number_of_options == 5:
      BUTTON_ONE = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2,
                          text_input=chosen_encounter.encounter_option_list[0], font=get_font(25))
      BUTTON_TWO = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + 50,
                          text_input=chosen_encounter.encounter_option_list[1], font=get_font(25))
      BUTTON_THREE = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + 100,
                          text_input=chosen_encounter.encounter_option_list[2], font=get_font(25))
      BUTTON_FOUR = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + 150,
                          text_input=chosen_encounter.encounter_option_list[3], font=get_font(25))
      BUTTON_FIVE = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/2, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + 200,
                          text_input=chosen_encounter.encounter_option_list[4], font=get_font(25))
                                           
                          
      
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                def first_button():
                  if BUTTON_ONE.rect.collidepoint(mouse_pos):
                    if BUTTON_ONE.text_input.startswith("[Exit]"):
                      main_menu()
                    elif BUTTON_ONE.text_input.startswith("[Chance]"):
                      for value in chosen_encounter.chances_list:
                        if value == BUTTON_ONE.text_input:
                          i = chosen_encounter.chances_list.index(value)
                          number = randint(0, 100)
                          if number >= 51:
                            encounter_results(chosen_encounter.first_results[i])
                            pass # for currency
                            pass # for health
                          elif number < 51 and chosen_encounter.second_results != []:
                            encounter_results(chosen_encounter.second_results[i])
                            pass # for currency
                            pass # for health
                    elif BUTTON_ONE.text_input.startswith("[Item/Weaponry]"):
                      for value in chosen_encounter.items_list:
                        if value == BUTTON_ONE.text_input:
                          i = chosen_encounter.items_list.index(value)
                          encounter_results(chosen_encounter.usable_results[i])
                          pass # for currency
                          pass # for removing item/weapon
                    elif BUTTON_ONE.text_input.startswith("[Dialogue]"):
                      for value in chosen_encounter.dialogues_list:
                        if value == BUTTON_ONE.text_input:
                          i = chosen_encounter.dialogues_list.index(value)
                          encounter_results(chosen_encounter.responses[i])
                          pass # for currency
                          pass # for health
                    elif BUTTON_ONE.text_input.startswith("[Battle]"):
                      pass
                    elif BUTTON_ONE.text_input.startswith("[Give In]"):
                      pass
                    
                def second_button():
                  if BUTTON_TWO.rect.collidepoint(mouse_pos):
                    if BUTTON_TWO.text_input.startswith("[Exit]"):
                      main_menu()
                    elif BUTTON_TWO.text_input.startswith("[Chance]"):
                      for value in chosen_encounter.chances_list:
                        if value == BUTTON_TWO.text_input:
                          i = chosen_encounter.chances_list.index(value)
                          number = randint(0, 100)
                          if number >= 51:
                            encounter_results(chosen_encounter.first_results[i])
                            pass # for currency
                            pass # for health
                          elif number < 51 and chosen_encounter.second_results != []:
                            encounter_results(chosen_encounter.second_results[i])
                            pass # for currency
                            pass # for health
                    elif BUTTON_TWO.text_input.startswith("[Item/Weaponry]"):
                      for value in chosen_encounter.items_list:
                        if value == BUTTON_TWO.text_input:
                          i = chosen_encounter.items_list.index(value)
                          encounter_results(chosen_encounter.usable_results[i])
                          pass # for currency
                          pass # for removing item/weapon
                    elif BUTTON_TWO.text_input.startswith("[Dialogue]"):
                      for value in chosen_encounter.dialogues_list:
                        if value == BUTTON_TWO.text_input:
                          i = chosen_encounter.dialogues_list.index(value)
                          encounter_results(chosen_encounter.responses[i])
                          pass # for currency
                          pass # for health
                    elif BUTTON_TWO.text_input.startswith("[Battle]"):
                      pass
                    elif BUTTON_TWO.text_input.startswith("[Give In]"):
                      pass
                      
                def third_button():
                  if BUTTON_THREE.rect.collidepoint(mouse_pos):
                    if BUTTON_THREE.text_input.startswith("[Exit]"):
                      main_menu()
                    elif BUTTON_THREE.text_input.startswith("[Chance]"):
                      for value in chosen_encounter.chances_list:
                        if value == BUTTON_THREE.text_input:
                          i = chosen_encounter.chances_list.index(value)
                          number = randint(0, 100)
                          if number >= 51:
                            encounter_results(chosen_encounter.first_results[i])
                            pass # for currency
                            pass # for health
                          elif number < 51 and chosen_encounter.second_results != []:
                            encounter_results(chosen_encounter.second_results[i])
                            pass # for currency
                            pass # for health
                    elif BUTTON_THREE.text_input.startswith("[Item/Weaponry]"):
                      for value in chosen_encounter.items_list:
                        if value == BUTTON_THREE.text_input:
                          i = chosen_encounter.items_list.index(value)
                          encounter_results(chosen_encounter.usable_results[i])
                          pass # for currency
                          pass # for removing item/weapon
                    elif BUTTON_THREE.text_input.startswith("[Dialogue]"):
                      for value in chosen_encounter.dialogues_list:
                        if value == BUTTON_THREE.text_input:
                          i = chosen_encounter.dialogues_list.index(value)
                          encounter_results(chosen_encounter.responses[i])
                          pass # for currency
                          pass # for health
                    elif BUTTON_THREE.text_input.startswith("[Battle]"):
                      pass
                    elif BUTTON_THREE.text_input.startswith("[Give In]"):
                      pass
                      
                def fourth_button():
                  if BUTTON_FOUR.rect.collidepoint(mouse_pos):
                    if BUTTON_FOUR.text_input.startswith("[Exit]"):
                      main_menu()
                    elif BUTTON_FOUR.text_input.startswith("[Chance]"):
                      for value in chosen_encounter.chances_list:
                        if value == BUTTON_FOUR.text_input:
                          i = chosen_encounter.chances_list.index(value)
                          number = randint(0, 100)
                          if number >= 51:
                            encounter_results(chosen_encounter.first_results[i])
                            pass # for currency
                            pass # for health
                          elif number < 51 and chosen_encounter.second_results != []:
                            encounter_results(chosen_encounter.second_results[i])
                            pass # for currency
                            pass # for health
                    elif BUTTON_FOUR.text_input.startswith("[Item/Weaponry]"):
                      for value in chosen_encounter.items_list:
                        if value == BUTTON_FOUR.text_input:
                          i = chosen_encounter.items_list.index(value)
                          encounter_results(chosen_encounter.usable_results[i])
                          pass # for currency
                          pass # for removing item/weapon
                    elif BUTTON_FOUR.text_input.startswith("[Dialogue]"):
                      for value in chosen_encounter.dialogues_list:
                        if value == BUTTON_FOUR.text_input:
                          i = chosen_encounter.dialogues_list.index(value)
                          encounter_results(chosen_encounter.responses[i])
                          pass # for currency
                          pass # for health
                    elif BUTTON_FOUR.text_input.startswith("[Battle]"):
                      pass
                    elif BUTTON_FOUR.text_input.startswith("[Give In]"):
                      pass
                      
                def fifth_button():
                  if BUTTON_FIVE.rect.collidepoint(mouse_pos):
                    if BUTTON_FIVE.text_input.startswith("[Exit]"):
                      main_menu()
                    elif BUTTON_FIVE.text_input.startswith("[Chance]"):
                      for value in chosen_encounter.chances_list:
                        if value == BUTTON_FIVE.text_input:
                          i = chosen_encounter.chances_list.index(value)
                          number = randint(0, 100)
                          if number >= 51:
                            encounter_results(chosen_encounter.first_results[i])
                            pass # for currency
                            pass # for health
                          elif number < 51 and chosen_encounter.second_results != []:
                            encounter_results(chosen_encounter.second_results[i])
                            pass # for currency
                            pass # for health
                    elif BUTTON_FIVE.text_input.startswith("[Item/Weaponry]"):
                      for value in chosen_encounter.items_list:
                        if value == BUTTON_FIVE.text_input:
                          i = chosen_encounter.items_list.index(value)
                          encounter_results(chosen_encounter.usable_results[i])
                          pass # for currency
                          pass # for removing item/weapon
                    elif BUTTON_FIVE.text_input.startswith("[Dialogue]"):
                      for value in chosen_encounter.dialogues_list:
                        if value == BUTTON_FOUR.text_input:
                          i = chosen_encounter.dialogues_list.index(value)
                          encounter_results(chosen_encounter.responses[i])
                          pass # for currency
                          pass # for health
                    elif BUTTON_FIVE.text_input.startswith("[Battle]"):
                      pass
                    elif BUTTON_FIVE.text_input.startswith("[Give In]"):
                      pass
                      
                if chosen_encounter.number_of_options == 1:
                  first_button()

                elif chosen_encounter.number_of_options == 2:
                  first_button()
                  second_button()
                
                elif chosen_encounter.number_of_options == 3:
                  first_button()
                  second_button()
                  third_button()
                
                elif chosen_encounter.number_of_options == 4:
                  first_button()
                  second_button()
                  third_button()
                  fourth_button()

                elif chosen_encounter.number_of_options == 5:
                  first_button()
                  second_button()
                  third_button()
                  fourth_button()
                  fifth_button()
                  
        screen.fill((255, 255, 255))
        BG = pygame.image.load("images\\space.jpg")
        BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(BG, (0, 0))
        MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.020), None).render(chosen_encounter.description, True, "white")
        screen.blit(MENU_TEXT, (int(SCREEN_WIDTH * 0.5) - MENU_TEXT.get_width() // 2, int(SCREEN_HEIGHT * 0.25) - MENU_TEXT.get_height() // 2))

        if chosen_encounter.number_of_options == 1:
          BUTTON_ONE.update(screen)
          
        elif chosen_encounter.number_of_options == 2:
          BUTTON_ONE.update(screen)
          BUTTON_TWO.update(screen)

        elif chosen_encounter.number_of_options == 3:
          BUTTON_ONE.update(screen)
          BUTTON_TWO.update(screen)
          BUTTON_THREE.update(screen)

        elif chosen_encounter.number_of_options == 4:
          BUTTON_ONE.update(screen)
          BUTTON_TWO.update(screen)
          BUTTON_THREE.update(screen)
          BUTTON_FOUR.update(screen)
          
        elif chosen_encounter.number_of_options == 5:
          BUTTON_ONE.update(screen)
          BUTTON_TWO.update(screen)
          BUTTON_THREE.update(screen)
          BUTTON_FOUR.update(screen)
          BUTTON_FIVE.update(screen)

        pygame.display.flip()

def encounter_results(text):
    pygame.display.set_caption("Encounter")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYDOWN:
          main_menu()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          main_menu()
    
      screen.fill((255, 255, 255))
      BG = pygame.image.load("images\\space.jpg")
      BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
      screen.blit(BG, (0, 0))
      MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.020), None).render(text, True, "white")
      screen.blit(MENU_TEXT, (int(SCREEN_WIDTH * 0.5) - MENU_TEXT.get_width() // 2, int(SCREEN_HEIGHT * 0.25) - MENU_TEXT.get_height() // 2))
        
      pygame.display.flip()





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
        MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.078), None).render("MAIN MENU", True, "White")
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
