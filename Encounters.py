# imported libraries
from random import randint
import textwrap
import sys
from Constants import *
import pygame
from Button import Button





def encounter_menu(SCREEN_WIDTH, SCREEN_HEIGHT):
    from SOT import main_menu
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
    from SOT import main_menu
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

# This list holds the encounters to be chosen.
encounter_list = []


# This is the Encounters class, which creates the encounters.
class Encounter:
  def __init__(self, type, name, description, number_of_options = 1):
    self.type = type
    self.name = name
    self.description = description
    self.number_of_options = number_of_options
    self.encounter_option_list = []
    self.dialogues_list = []
    self.chances_list = []
    self.items_list = []
    self.responses = []
    self.first_results = []
    self.second_results = []
    self.usable_names = []
    self.usable_results = []
    self.response_currency_changes = []
    self.response_health_changes = []
    self.first_result_currency_changes = []
    self.first_result_health_changes = []
    self.second_result_currency_changes = []
    self.second_result_health_changes = []
    self.usable_currency_changes = []
    encounter_list.append(self)
    
# These functions are the types of options that an encounter can have (what the player can choose).
  def Choices(self, type, description):
    text = type + " " + description
    self.encounter_option_list.append(text)
    if type == "[Dialogue]":
      self.dialogues_list.append(text)
    if type == "[Chance]":
      self.chances_list.append(text)
    if type == "[Item/Weaponry]":
      self.items_list.append(text)

  def Results(self, response = None, first_result = None, second_result = None, usable_name = None, usable_result = None, 
              response_currency_change = 0, response_health_change = 0, first_result_currency_change = 0, first_result_health_change = 0, second_result_currency_change = 0, second_result_health_change = 0, usable_currency_change = 0):
    if response != None:
      self.responses.append(response)
      self.response_currency_changes.append(response_currency_change)
      self.response_health_changes.append(response_health_change)
    elif first_result != None and second_result == None:
      self.first_results.append(first_result)
      self.first_result_currency_changes.append(first_result_currency_change)
      self.first_result_health_changes.append(first_result_health_change)
    elif first_result != None and second_result != None:
      self.first_results.append(first_result)
      self.first_result_currency_changes.append(first_result_currency_change)
      self.first_result_health_changes.append(first_result_health_change)
      self.second_results.append(second_result)
      self.second_result_currency_changes.append(second_result_currency_change)
      self.second_result_health_changes.append(second_result_health_change)
    elif usable_name != None:
      self.usable_names.append(usable_name)
      self.usable_results.append(usable_result)
      self.usable_currency_changes.append(usable_currency_change)
    
# This section is where encounters are initiated.
e1 = Encounter("Trade", "Example Shop", "This is a shop.", 1)
e1.Choices("[Exit]", "You can leave the shop with this button.")
e1.Choices("[Trade]", "You can initiate trade with this button.")

e2 = Encounter("Ship-based", "Yearly Celebration", textwrap.fill("""As you do yearly, your colony hosts the anneversary of the Space Warlord's death.
This time, however, it seems the colony wants to have a massive feast. Will you keep the celebration modest, or go all out?""", width=50), 2)
e2.Choices("[Dialogue]", "Allow a feast to be had! The more food the merrier, as they say.")
e2.Results("Though it was a bit costly, the colony appriciates it. It seems the colony even grew as a result.", None, None, None, None, -50, 10)
e2.Choices("[Dialogue]", "Keep things modest. You will all need to keep supplies for the journey ahead.")
e2.Results("It was a small celebration, one that wouldn't hurt the colony in any way. Though that's not to say some people weren't annoyed.")

e3 = Encounter("Event", "Astreoids", textwrap.fill("""Your colony approaches an asteroid field. The only way to get to your
 destination on time is to go through. Alternatively, you could change route and go around. What do you choose?""", width=50), 4)
e3.Choices("[Exit]", "Decide to go a different route.")
e3.Choices("[Chance]", "Decide to go through it anyways.")
e3.Results(None, "You succeeded in making it through! What a lucky break.", textwrap.fill("""Unfortunately, though you 
made it through the field, your ship took damage as a result, and some crew were lost.""", width=50), None, None, 0, 0, 0, 0, 0, -30)
e3.Choices("[Item/Weaponry]", "Fire away at the asteroids to clear a path.")
e3.Results(None, None, None, "Laser Cannons", "Firing your laser cannons, your ship blasts a clear path through the asteroids, making it out cleanly.")
e3.Choices("[Item/Weaponry]", "Overcharge the ship's reactor, giving it enough power to get through quick and unscathed.")
e3.Results(None, None, None, textwrap.fill("""Extra Reactor Core", "The core allowed for yoiur ship to get enough power 
           to charge through the field. Before you knew it, the ship was clear through.""",width=50))

e4 = Encounter("Event", "Abandoned Vessel", textwrap.fill("""As your ship charts its course, you come across an 
abandoned fleet of vessels which don't appear to have been picked clean. Valuable loot could be found here.""", width=50), 3)
e4.Choices("[Exit]", "Continue past the fleet. Not worth risking your lives for.")
e4.Choices("[Chance]", "Choose to explore the vessels.")
e4.Results(None, textwrap.fill("""Upon further inspection, the ship appeared to be infected from some virus. The crew, however, 
           managed to fight their way through without any losses. They even found plenty of loot!, 
          Upon entry, the crew was ambushed by the infected remains of the fleet's previous inhabitants, leading to heavy casualties.""", width=50), None, None, 0, 0, 100, 0, 0, -60)
e4.Choices("[Item/Weaponry]", "Using your acquired long range radio, you radio the nearest fleet to inform them of the wreckage.")
e4.Results(None, None, None, "Long-Range Radio", textwrap.fill("""A salvage and containment crew were contacted, upon which your colony 
           was rewarded for the information. They should be able to handle things on their own.""", width=50), 0, 0, 0, 0, 0, 0, 400)

e5 = Encounter("Battle", "Bandit Fleet", textwrap.fill("""Your colony comes across a group of bandit ships on its travels. 
               They radio over, 'Give us all of your valuables and gold, or we will destroy that puny ship of yours-'. What is your response?""", width=50), 5)
e5.Choices("[Dialogue]", "Uhm....who are you, exactly?")
e5.Results(textwrap.fill("""....are you stupid? Do you really not know what a robbery is? Fucking colonists these days. 
           We  are  taking  your  stuff  or  killing  you  all. Got it now?""", width=50))
e5.Choices("[Give In]", textwrap.fill("""You conceide, allowing the bandits to dock aboard the ship to get 
           whatever they want. They don't hurt anyone, but you are now mostly broke and resourceless.""", width=50))
e5.Choices("[Chance]", "You attempt to persuade the bandits to let you go.")
e5.Results(None, textwrap.fill("""*a sigh can be heard over the radio*  'Okay, you know what? I don't have 
           time to deal with this today. Consider this your lucky break.' They end up leaving your ship alone, for the time being.", 
                 "'HAH! Seriously?! You think we would let you off that easy? Boys, prepare to blast this junk outta my face.' You 
           take signifigant casualties from the sudden barrage of fire, and are boarded afterwards.""", width=50), None, None, 0, 0, 0, 0, -1000, -600)
e5.Choices("[Item/Weaponry]", "Your obvious firepower makes you wonder why they even attempted this.")
e5.Results(None, None, None, textwrap.fill("""Heavy Rocket Pods", "*some voices can be heard in the background* 'Ah, 
           right....yes....really? Fuck....alright, you all get to live another day. But next time, next time....be prepared.' The bandits leave your ship alone.""", width=50))
e5.Choices("[Battle]", "No one attempts to attack your colony without punishment. To your stations!")


def choose_encounter():
  # This section chooses the encounter to display
  random_number = randint(0, len(encounter_list)-1)
  chosen_encounter = encounter_list[random_number]
  return chosen_encounter

def run_encounter(SCREEN_WIDTH, SCREEN_HEIGHT):
  choose_encounter()
  encounter_menu(SCREEN_WIDTH, SCREEN_HEIGHT)

def choose_shop():
  random_number = 0
  chosen_encounter = encounter_list[random_number]
  return chosen_encounter

def run_shop(SCREEN_WIDTH, SCREEN_HEIGHT):
  global chosen_encounter
  chosen_encounter = choose_shop()
  encounter_menu(SCREEN_WIDTH, SCREEN_HEIGHT)

def choose_peaceful():
  random_number = 1
  chosen_encounter = encounter_list[random_number]
  return chosen_encounter

def run_peaceful(SCREEN_WIDTH, SCREEN_HEIGHT):
  global chosen_encounter
  chosen_encounter = choose_peaceful()
  encounter_menu(SCREEN_WIDTH, SCREEN_HEIGHT)

def choose_event():
  random_number = randint(2, 3)
  chosen_encounter = encounter_list[random_number]
  return chosen_encounter

def run_event(SCREEN_WIDTH, SCREEN_HEIGHT):
  global chosen_encounter
  chosen_encounter =choose_event()
  encounter_menu(SCREEN_WIDTH, SCREEN_HEIGHT)

def choose_hostile():
  random_number = 4
  chosen_encounter = encounter_list[random_number]
  return chosen_encounter

def run_hostile(SCREEN_WIDTH, SCREEN_HEIGHT):
  global chosen_encounter
  chosen_encounter =choose_hostile()
  encounter_menu(SCREEN_WIDTH, SCREEN_HEIGHT)

shop = [e1]
peaceful = [e2]
event = [e3, e4]
hostile = [e5]


