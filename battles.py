# import the required libraries
import pygame
import sys
import pygame_menu as pm
from Constants import *
from Armor_Health_and_Move_Systems import *
from random import randint
from Button import *

button = "images\\button.png"



def battle(opponent, player = P1):
    pygame.display.set_caption("Battle")
    from SOT import main_menu, SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    running = True
    PLAYER_SHIP = Image(image=pygame.transform.scale(pygame.image.load(player.image), (SCREEN_WIDTH/5, SCREEN_WIDTH/5)),
                          x_pos=SCREEN_WIDTH // 2 - 450, y_pos=SCREEN_HEIGHT // 2 + 50)
                          
    ENEMY_SHIP = Image(image=pygame.transform.scale(pygame.image.load(opponent.image), (SCREEN_WIDTH/5, SCREEN_WIDTH/5)),
                          x_pos=SCREEN_WIDTH // 2 + 450, y_pos=SCREEN_HEIGHT // 2 - 200)
    PLAYER_HEALTH = StatusBar(player.current_Health, player.max_Health, x_pos=PLAYER_SHIP.x_pos + SCREEN_WIDTH/6, y_pos=PLAYER_SHIP.y_pos, width=SCREEN_WIDTH // 10, 
                          height=SCREEN_HEIGHT // 40)
    PLAYER_ARMOR = StatusBar(player.current_Armor, player.max_Armor, x_pos=PLAYER_SHIP.x_pos + SCREEN_WIDTH/6, y_pos=PLAYER_HEALTH.y_pos - SCREEN_HEIGHT//17, width=SCREEN_WIDTH // 10, 
                          height=SCREEN_HEIGHT // 40)
    ENEMY_HEALTH = StatusBar(opponent.current_Health, opponent.max_Health, x_pos=ENEMY_SHIP.x_pos - SCREEN_WIDTH/5, y_pos=ENEMY_SHIP.y_pos, width=SCREEN_WIDTH // 10, 
                          height=SCREEN_HEIGHT // 40)
    ENEMY_ARMOR = StatusBar(opponent.current_Armor, opponent.max_Armor, x_pos=ENEMY_SHIP.x_pos - SCREEN_WIDTH/5, y_pos=ENEMY_SHIP.y_pos - SCREEN_HEIGHT//17, width=SCREEN_WIDTH // 10, 
                          height=SCREEN_HEIGHT // 40)
                          
    P_HEALTH_TEXT = Text(x_pos=PLAYER_HEALTH.x_pos - 50, y_pos=PLAYER_HEALTH.y_pos, text_input="Healh:", font=get_font(25))
    P_ARMOR_TEXT = Text(x_pos=PLAYER_ARMOR.x_pos - 50, y_pos=PLAYER_ARMOR.y_pos, text_input="Armor:", font=get_font(25))
    O_HEALTH_TEXT = Text(x_pos= ENEMY_HEALTH.x_pos - 50, y_pos=ENEMY_HEALTH.y_pos, text_input="Health:", font=get_font(25))
    O_ARMOR_TEXT = Text(x_pos=ENEMY_ARMOR.x_pos - 50, y_pos=ENEMY_ARMOR.y_pos, text_input="Armor:", font=get_font(25))

    FIGHT_BUTTON = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/7, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2 - SCREEN_WIDTH//10, y_pos=SCREEN_HEIGHT // 2 + SCREEN_HEIGHT/3,
                          text_input="FIGHT", font=get_font(25))
    
    RUN_BUTTON = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/7, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2 + SCREEN_WIDTH//10, y_pos=SCREEN_HEIGHT // 2 + SCREEN_HEIGHT/3,
                          text_input="RUN", font=get_font(25))
    
    
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
                if FIGHT_BUTTON.rect.collidepoint(mouse_pos):
                  moves_screen(player, opponent, player)
                elif RUN_BUTTON.rect.collidepoint(mouse_pos):
                  chance = randint(0, 100)
                  if chance >= 51:
                    battle_transitions("You successfully managed to escape-", "run_pass", opponent, player)
                  else:
                    battle_transitions("Unfortunately, your escape attempt failed-", "run_fail", opponent, player)
                    
        screen.fill((255, 255, 255))
        BG = pygame.image.load("images\\hud.png")
        BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(BG, (0, 0))
        MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.020), None).render("", True, "white")
        screen.blit(MENU_TEXT, (int(SCREEN_WIDTH * 0.5) - MENU_TEXT.get_width() // 2, int(SCREEN_HEIGHT * 0.25) - MENU_TEXT.get_height() // 2))
        
        P_HEALTH_TEXT.update(screen)
        P_ARMOR_TEXT.update(screen)
        O_HEALTH_TEXT.update(screen)
        O_ARMOR_TEXT.update(screen)
        PLAYER_HEALTH.update(screen)
        PLAYER_ARMOR.update(screen)
        ENEMY_HEALTH.update(screen)
        ENEMY_ARMOR.update(screen)
        PLAYER_SHIP.update(screen)
        ENEMY_SHIP.update(screen)
        FIGHT_BUTTON.update(screen)
        RUN_BUTTON.update(screen)
        pygame.display.flip()
    
    
def moves_screen(starter, opponent, player):
    pygame.display.set_caption("Battle")
    from SOT import main_menu, SCREEN_HEIGHT, SCREEN_WIDTH
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    order_list = []
    
    if starter == player:
      order_list = [player, opponent]
    elif starter == opponent:
      order_list = [opponent, player]
    
    running = True
    PLAYER_SHIP = Image(image=pygame.transform.scale(pygame.image.load(player.image), (SCREEN_WIDTH/5, SCREEN_WIDTH/5)),
                          x_pos=SCREEN_WIDTH // 2 - 450, y_pos=SCREEN_HEIGHT // 2 + 50)
                          
    ENEMY_SHIP = Image(image=pygame.transform.scale(pygame.image.load(opponent.image), (SCREEN_WIDTH/5, SCREEN_WIDTH/5)),
                          x_pos=SCREEN_WIDTH // 2 + 450, y_pos=SCREEN_HEIGHT // 2 - 200)
    PLAYER_HEALTH = StatusBar(player.current_Health, player.max_Health, x_pos=PLAYER_SHIP.x_pos + SCREEN_WIDTH/6, y_pos=PLAYER_SHIP.y_pos, width=SCREEN_WIDTH // 10, 
                          height=SCREEN_HEIGHT // 40)
    PLAYER_ARMOR = StatusBar(player.current_Armor, player.max_Armor, x_pos=PLAYER_SHIP.x_pos + SCREEN_WIDTH/6, y_pos=PLAYER_HEALTH.y_pos - SCREEN_HEIGHT//17, width=SCREEN_WIDTH // 10, 
                          height=SCREEN_HEIGHT // 40)
    ENEMY_HEALTH = StatusBar(opponent.current_Health, opponent.max_Health, x_pos=ENEMY_SHIP.x_pos - SCREEN_WIDTH/5, y_pos=ENEMY_SHIP.y_pos, width=SCREEN_WIDTH // 10, 
                          height=SCREEN_HEIGHT // 40)
    ENEMY_ARMOR = StatusBar(opponent.current_Armor, opponent.max_Armor, x_pos=ENEMY_SHIP.x_pos - SCREEN_WIDTH/5, y_pos=ENEMY_SHIP.y_pos - SCREEN_HEIGHT//17, width=SCREEN_WIDTH // 10, 
                          height=SCREEN_HEIGHT // 40)
                          
    P_HEALTH_TEXT = Text(x_pos=PLAYER_HEALTH.x_pos - 50, y_pos=PLAYER_HEALTH.y_pos, text_input="Healh:", font=get_font(25))
    P_ARMOR_TEXT = Text(x_pos=PLAYER_ARMOR.x_pos - 50, y_pos=PLAYER_ARMOR.y_pos, text_input="Armor:", font=get_font(25))
    O_HEALTH_TEXT = Text(x_pos= ENEMY_HEALTH.x_pos - 50, y_pos=ENEMY_HEALTH.y_pos, text_input="Health:", font=get_font(25))
    O_ARMOR_TEXT = Text(x_pos=ENEMY_ARMOR.x_pos - 50, y_pos=ENEMY_ARMOR.y_pos, text_input="Armor:", font=get_font(25))
                          
    ENEMY_SHIP = Image(image=pygame.transform.scale(pygame.image.load(opponent.image), (SCREEN_WIDTH/5, SCREEN_WIDTH/5)),
                          x_pos=SCREEN_WIDTH // 2 + 450, y_pos=SCREEN_HEIGHT // 2 - 200)
    FIRST_MOVE = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/7, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2 - SCREEN_WIDTH//10, y_pos=SCREEN_HEIGHT // 2 + SCREEN_HEIGHT/3,
                          text_input=player_moves_list[0].Move_Name, font=get_font(25))
    
    SECOND_MOVE = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/7, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2 + SCREEN_WIDTH//10, y_pos=SCREEN_HEIGHT // 2 + SCREEN_HEIGHT/3,
                          text_input=player_moves_list[1].Move_Name, font=get_font(25))
                          
    THIRD_MOVE = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/7, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2 - SCREEN_WIDTH//10, y_pos=SCREEN_HEIGHT // 2 + 4*SCREEN_HEIGHT/9,
                          text_input=player_moves_list[2].Move_Name, font=get_font(25))
    
    FOURTH_MOVE = Button(image=pygame.transform.scale(BUTTON, (SCREEN_WIDTH/7, SCREEN_HEIGHT/15)),
                          x_pos=SCREEN_WIDTH // 2 + SCREEN_WIDTH//10, y_pos=SCREEN_HEIGHT // 2 + 4*SCREEN_HEIGHT/9,
                          text_input=player_moves_list[3].Move_Name, font=get_font(25))
    
    if player.current_Health <= 0:
      battle_transitions("Having lost all of its crew, your vessel was destroyed. GAME OVER", "battle_lose", opponent, player)
    elif opponent.current_Health <= 0:
      battle_transitions("You've defeated your opponent, nice work. YOU WIN!", "battle_win", opponent, player)
    
    while running:
        if order_list[0] == opponent:
          if opponent.current_Health <= .5 * opponent.max_Health:
            heal_chance = 90
            if randint(0, 100) >= heal_chance:
              for move in opponent_moves_list:
                if move.Move_Name.endswith("Heal"):
                  move.use_Heal_Move(opponent)
                  battle_transitions(opponent.name + " used " + move.Move_Name, "used_heal", opponent, player, opponent)
            else:
              attacks = [move for move in opponent_moves_list if move.Move_Name.endswith("Heal") == False and move.Move_Name.endswith("Repair") == False]
              random_num = randint(0, len(attacks) - 1)
              chosen_attack = attacks[random_num]
              chosen_attack.use_Attack_Move(player)
              battle_transitions(opponent.name + " used " + chosen_attack.Move_Name, "used_attack", opponent, player, opponent, chosen_attack)
          elif opponent.current_Armor <= .25 * opponent.max_Armor:
            repair_chance = 80
            if randint(0, 100) >= repair_chance:
              for move in opponent_moves_list:
                if move.Move_Name.endswith("Repair"):
                  move.use_Repair_Move(opponent)
                  battle_transitions(opponent.name + " used " + move.Move_Name, "used_heal", opponent, player, opponent)
            else:
              attacks = [move for move in opponent_moves_list if move.Move_Name.endswith("Heal") == False and move.Move_Name.endswith("Repair") == False]
              random_num = randint(0, len(attacks) - 1)
              chosen_attack = attacks[random_num]
              chosen_attack.use_Attack_Move(player)
              battle_transitions(opponent.name + " used " + chosen_attack.Move_Name, "used_attack", opponent, player, opponent, chosen_attack)
          else:
            attacks = [move for move in opponent_moves_list if move.Move_Name.endswith("Heal") == False and move.Move_Name.endswith("Repair") == False]
            random_num = randint(0, len(attacks) - 1)
            chosen_attack = attacks[random_num]
            chosen_attack.use_Attack_Move(player)
            battle_transitions(opponent.name + " used " + chosen_attack.Move_Name, "used_attack", opponent, player, opponent, chosen_attack)
        elif order_list[0] == player:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
              elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_ESCAPE:
                      main_menu()
              elif event.type == pygame.MOUSEBUTTONDOWN:
                  mouse_pos = pygame.mouse.get_pos()
                  if FIRST_MOVE.rect.collidepoint(mouse_pos):
                    if player_moves_list[0].Move_Name.endswith("Heal"):
                      player_moves_list[0].use_Heal_Move(player)
                      battle_transitions(player.name + " used " + player_moves_list[0].Move_Name, "used_heal", opponent, player, player)
                    elif player_moves_list[0].Move_Name.endswith("Repair"):
                      player_moves_list[0].use_Repair_Move(player)
                      battle_transitions(player.name + " used " + player_moves_list[0].Move_Name, "used_heal", opponent, player, player)
                    else:
                      player_moves_list[0].use_Attack_Move(opponent)
                      battle_transitions(player.name + " used " + player_moves_list[0].Move_Name, "used_attack", opponent, player, player, player_moves_list[0])
                  elif SECOND_MOVE.rect.collidepoint(mouse_pos):
                    if player_moves_list[1].Move_Name.endswith("Heal"):
                      player_moves_list[1].use_Heal_Move(player)
                      battle_transitions(player.name + " used " + player_moves_list[1].Move_Name, "used_heal", opponent, player, player)
                    elif player_moves_list[1].Move_Name.endswith("Repair"):
                      player_moves_list[1].use_Repair_Move(player)
                      battle_transitions(player.name + " used " + player_moves_list[1].Move_Name, "used_heal", opponent, player, player)
                    else:
                      player_moves_list[1].use_Attack_Move(opponent)
                      battle_transitions(player.name + " used " + player_moves_list[1].Move_Name, "used_attack", opponent, player, player, player_moves_list[1])
                  elif THIRD_MOVE.rect.collidepoint(mouse_pos):
                    if player_moves_list[2].Move_Name.endswith("Heal"):
                      player_moves_list[2].use_Heal_Move(player)
                      battle_transitions(player.name + " used " + player_moves_list[2].Move_Name, "used_heal", opponent, player, player)
                    elif player_moves_list[2].Move_Name.endswith("Repair"):
                      player_moves_list[2].use_Repair_Move(player)
                      battle_transitions(player.name + " used " + player_moves_list[2].Move_Name, "used_heal", opponent, player, player)
                    else:
                      player_moves_list[2].use_Attack_Move(opponent)
                      battle_transitions(player.name + " used " + player_moves_list[2].Move_Name, "used_attack", opponent, player, player, player_moves_list[0])
                  elif FOURTH_MOVE.rect.collidepoint(mouse_pos):
                    if player_moves_list[3].Move_Name.endswith("Heal"):
                      player_moves_list[3].use_Heal_Move(player)
                      battle_transitions(player.name + " used " + player_moves_list[3].Move_Name, "used_heal", opponent, player, player)
                    elif player_moves_list[3].Move_Name.endswith("Repair"):
                      player_moves_list[3].use_Repair_Move(player)
                      battle_transitions(player.name + " used " + player_moves_list[3].Move_Name, "used_heal", opponent, player, player)
                    else:
                      player_moves_list[3].use_Attack_Move(opponent)
                      battle_transitions(player.name + " used " + player_moves_list[3].Move_Name, "used_attack", opponent, player, player, player_moves_list[0])
                    
        screen.fill((255, 255, 255))
        BG = pygame.image.load("images\\hud.png")
        BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(BG, (0, 0))
        MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.020), None).render("", True, "white")
        screen.blit(MENU_TEXT, (int(SCREEN_WIDTH * 0.5) - MENU_TEXT.get_width() // 2, int(SCREEN_HEIGHT * 0.25) - MENU_TEXT.get_height() // 2))
        
        
        P_HEALTH_TEXT.update(screen)
        P_ARMOR_TEXT.update(screen)
        O_HEALTH_TEXT.update(screen)
        O_ARMOR_TEXT.update(screen)
        PLAYER_HEALTH.update(screen)
        PLAYER_ARMOR.update(screen)
        ENEMY_HEALTH.update(screen)
        ENEMY_ARMOR.update(screen)
        PLAYER_SHIP.update(screen)
        ENEMY_SHIP.update(screen)
        FIRST_MOVE.update(screen)
        SECOND_MOVE.update(screen)
        THIRD_MOVE.update(screen)
        FOURTH_MOVE.update(screen)
        pygame.display.flip()
    
    
    
    
    
    
def battle_transitions(text, designator, opponent, player, current_turn = None, move = None):
    pygame.display.set_caption("Encounter")
    from SOT import main_menu, SCREEN_WIDTH, SCREEN_HEIGHT
    from map_module import run_map
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    
    running = True
    PLAYER_SHIP = Image(image=pygame.transform.scale(pygame.image.load(player.image), (SCREEN_WIDTH/5, SCREEN_WIDTH/5)),
                          x_pos=SCREEN_WIDTH // 2 - 450, y_pos=SCREEN_HEIGHT // 2 + 50)
                          
    ENEMY_SHIP = Image(image=pygame.transform.scale(pygame.image.load(opponent.image), (SCREEN_WIDTH/5, SCREEN_WIDTH/5)),
                          x_pos=SCREEN_WIDTH // 2 + 450, y_pos=SCREEN_HEIGHT // 2 - 200)
    PLAYER_HEALTH = StatusBar(player.current_Health, player.max_Health, x_pos=PLAYER_SHIP.x_pos + SCREEN_WIDTH/6, y_pos=PLAYER_SHIP.y_pos, width=SCREEN_WIDTH // 10, 
                          height=SCREEN_HEIGHT // 40)
    PLAYER_ARMOR = StatusBar(player.current_Armor, player.max_Armor, x_pos=PLAYER_SHIP.x_pos + SCREEN_WIDTH/6, y_pos=PLAYER_HEALTH.y_pos - SCREEN_HEIGHT//17, width=SCREEN_WIDTH // 10, 
                          height=SCREEN_HEIGHT // 40)
    ENEMY_HEALTH = StatusBar(opponent.current_Health, opponent.max_Health, x_pos=ENEMY_SHIP.x_pos - SCREEN_WIDTH/5, y_pos=ENEMY_SHIP.y_pos, width=SCREEN_WIDTH // 10, 
                          height=SCREEN_HEIGHT // 40)
    ENEMY_ARMOR = StatusBar(opponent.current_Armor, opponent.max_Armor, x_pos=ENEMY_SHIP.x_pos - SCREEN_WIDTH/5, y_pos=ENEMY_SHIP.y_pos - SCREEN_HEIGHT//17, width=SCREEN_WIDTH // 10, 
                          height=SCREEN_HEIGHT // 40)
                          
    P_HEALTH_TEXT = Text(x_pos=PLAYER_HEALTH.x_pos - 50, y_pos=PLAYER_HEALTH.y_pos, text_input="Healh:", font=get_font(25))
    P_ARMOR_TEXT = Text(x_pos=PLAYER_ARMOR.x_pos - 50, y_pos=PLAYER_ARMOR.y_pos, text_input="Armor:", font=get_font(25))
    O_HEALTH_TEXT = Text(x_pos= ENEMY_HEALTH.x_pos - 50, y_pos=ENEMY_HEALTH.y_pos, text_input="Health:", font=get_font(25))
    O_ARMOR_TEXT = Text(x_pos=ENEMY_ARMOR.x_pos - 50, y_pos=ENEMY_ARMOR.y_pos, text_input="Armor:", font=get_font(25))
    BOTTOM_TEXT = Text(x_pos=SCREEN_WIDTH // 2, y_pos=SCREEN_HEIGHT // 2 + SCREEN_HEIGHT//4, text_input=text, font=get_font(25))
    
    while running:
      if designator == "run_pass":
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
          elif event.type == pygame.KEYDOWN:
            if pygame.KEYDOWN == pygame.K_ESCAPE:
              main_menu()
          elif event.type == pygame.MOUSEBUTTONDOWN:
            run_map(SCREEN_WIDTH, SCREEN_HEIGHT)
      elif designator == "battle_win":
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
          elif event.type == pygame.KEYDOWN:
            if pygame.KEYDOWN == pygame.K_ESCAPE:
              main_menu()
          elif event.type == pygame.MOUSEBUTTONDOWN:
            run_map(SCREEN_WIDTH, SCREEN_HEIGHT)
      elif designator == "run_fail":
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
          elif event.type == pygame.KEYDOWN:
            main_menu()
          elif event.type == pygame.MOUSEBUTTONDOWN:
            battle(opponent)
      elif designator == "battle_lose":
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
          elif event.type == pygame.KEYDOWN:
            main_menu()
          elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()
      elif designator == "used_attack":
        if move.success == True:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
              main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
              battle_transitions("It hits!", "attack_end", opponent, player, current_turn)
        elif move.success == False:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
              main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
              battle_transitions("A miss!", "attack_end", opponent, player, current_turn)
      elif designator == "attack_end":
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
          elif event.type == pygame.KEYDOWN:
            main_menu()
          elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_turn == opponent:
              moves_screen(player, opponent, player)
            elif current_turn == player:
              moves_screen(opponent, opponent, player)
              
      elif designator == "used_heal":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
              main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
              if current_turn == opponent:
                moves_screen(player, opponent, player)
              elif current_turn == player:
                moves_screen(opponent, opponent, player)

      screen.fill((255, 255, 255))
      BG = pygame.image.load("images\\hud.png")
      BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
      screen.blit(BG, (0, 0))
      MENU_TEXT = get_font(int(SCREEN_WIDTH * 0.020), None).render("", True, "white")
      screen.blit(MENU_TEXT, (int(SCREEN_WIDTH * 0.5) - MENU_TEXT.get_width() // 2, int(SCREEN_HEIGHT * 0.25) - MENU_TEXT.get_height() // 2))
      
      P_HEALTH_TEXT.update(screen)
      P_ARMOR_TEXT.update(screen)
      O_HEALTH_TEXT.update(screen)
      O_ARMOR_TEXT.update(screen)
      PLAYER_HEALTH.update(screen)
      PLAYER_ARMOR.update(screen)
      ENEMY_HEALTH.update(screen)
      ENEMY_ARMOR.update(screen)
      PLAYER_SHIP.update(screen)
      ENEMY_SHIP.update(screen)
      BOTTOM_TEXT.update(screen)
      pygame.display.flip()