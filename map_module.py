from random import randint, seed, choice
import pygame
from Constants import *
from Encounters import *
import json
import os
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN
)



def run_map(SCREEN_WIDTH, SCREEN_HEIGHT):
    from SOT import main_menu
    # Initialize pygame
    pygame.init()
    global chosen_encounter
    # Define constants for the screen width and height


    # Create the screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Variable to keep the main loop running
    running = True

    # Define constants for map tile sizes
    MAP_TILE_WIDTH = SCREEN_WIDTH // 6
    MAP_TILE_HEIGHT = SCREEN_HEIGHT // 5

    # Define constants for map tile types and their ranges
    TILE_RANGES = {
        (0, 50): 0,  # Empty
        (51, 65): 1,  # Peaceful encounter
        (66, 89): 2,  # Hostile encounter
        (90, 95): 3,  # Event
        (96, 100): 4,  # Shop
    }

    # Load the image for unknown tiles
    unknown_img = pygame.image.load("images\\unknown.png")
    # Resize the image to fit the tile size
    unknown_img = pygame.transform.scale(unknown_img, (MAP_TILE_WIDTH, MAP_TILE_HEIGHT))

    # Load the image for empty tiles
    empty_img = pygame.image.load("images\\empty.png")
    # Resize the image to fit the tile size
    empty_img = pygame.transform.scale(empty_img, (MAP_TILE_WIDTH, MAP_TILE_HEIGHT))

    # Load the image for empty tiles
    peaceful_img = pygame.image.load("images\\peaceful.png")
    # Resize the image to fit the tile size
    peaceful_img = pygame.transform.scale(peaceful_img, (MAP_TILE_WIDTH, MAP_TILE_HEIGHT))

    # Load the image for empty tiles
    hostile_img = pygame.image.load("images\\hostile.png")
    # Resize the image to fit the tile size
    hostile_img = pygame.transform.scale(hostile_img, (MAP_TILE_WIDTH, MAP_TILE_HEIGHT))

    # Load the image for empty tiles
    shop_img = pygame.image.load("images\\shop.png")
    # Resize the image to fit the tile size
    shop_img = pygame.transform.scale(shop_img, (MAP_TILE_WIDTH, MAP_TILE_HEIGHT))

    # Load the image for empty tiles
    event_img = pygame.image.load("images\\event.png")
    # Resize the image to fit the tile size
    event_img = pygame.transform.scale(event_img, (MAP_TILE_WIDTH, MAP_TILE_HEIGHT))


    # Generate map tiles
    seed(randint(0, 1000))  # Seed for map generation
    map_tiles = []
    hidden_tiles = []  # Store the hidden tile types
    for _ in range(5):
        row = []
        hidden_row = []
        for _ in range(6):
            if randint(1, 10) <= 2:  # 20% chance of being hidden
                row.append(-1)  # -1 indicates hidden
                hidden_row.append(choice([1, 2, 3, 4]))  # Randomly choose a hidden tile type
            else:
                random_value = randint(0, 100)
                for (start, end), tile_type in TILE_RANGES.items():
                    if start <= random_value <= end:
                        row.append(tile_type)
                        hidden_row.append(None)  # No hidden tile
                        break
        map_tiles.append(row)
        hidden_tiles.append(hidden_row)

    # Main loop
    while running:
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    main_menu()
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False
            # Did the user click the mouse?
            elif event.type == MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Calculate the row and column of the clicked tile
                clicked_row = mouse_y // MAP_TILE_HEIGHT
                clicked_col = mouse_x // MAP_TILE_WIDTH
                # Get the tile type of the clicked tile
                tile_type = map_tiles[clicked_row][clicked_col]
                # If the tile is hidden, reveal it and activate
                if tile_type == -1:
                    # If hidden, activate the hidden tile
                    hidden_type = hidden_tiles[clicked_row][clicked_col]
                    if hidden_type is not None:  # Check if there's a hidden encounter
                        map_tiles[clicked_row][clicked_col] = hidden_type  # Set the tile to the hidden type
                        if hidden_type == 1:
                            run_peaceful(SCREEN_WIDTH, SCREEN_HEIGHT)
                            print("You activated a peaceful encounter!")
                        elif hidden_type == 2:
                            run_hostile(SCREEN_WIDTH, SCREEN_HEIGHT)
                            print("You activated a hostile encounter!")
                        elif hidden_type == 3:
                            run_event(SCREEN_WIDTH, SCREEN_HEIGHT)
                            print("You activated an event!")
                        elif hidden_type == 4:
                            run_shop(SCREEN_WIDTH, SCREEN_HEIGHT)
                            print("You activated a shop!")
                else:
                    if tile_type == 1:
                        run_peaceful(SCREEN_WIDTH, SCREEN_HEIGHT)
                        print("You activated a peaceful encounter!")
                    elif tile_type == 2:
                        run_hostile(SCREEN_WIDTH, SCREEN_HEIGHT)
                        print("You activated a hostile encounter!")
                    elif tile_type == 3:
                        run_event(SCREEN_WIDTH, SCREEN_HEIGHT)
                        print("You activated an event!")
                    elif tile_type == 4:
                        run_shop(SCREEN_WIDTH, SCREEN_HEIGHT)
                        print("You activated a shop!")

        # Fill the screen with white
        screen.fill((255, 255, 255))

        # Draw map tiles
        for row in range(5):
            for col in range(6):
                tile_type = map_tiles[row][col]
                if tile_type == -1:
                    # Draw hidden tile as grey
                    screen.blit(unknown_img, (col * MAP_TILE_WIDTH, row * MAP_TILE_HEIGHT))
                else:
                    # Draw revealed tiles based on their type
                    if tile_type == 0:
                        screen.blit(empty_img, (col * MAP_TILE_WIDTH, row * MAP_TILE_HEIGHT))  # White for empty tile
                    elif tile_type == 1:
                        screen.blit(peaceful_img, (col * MAP_TILE_WIDTH, row * MAP_TILE_HEIGHT))  # Green for peaceful encounter
                    elif tile_type == 2:
                        screen.blit(hostile_img, (col * MAP_TILE_WIDTH, row * MAP_TILE_HEIGHT))  # Red for hostile encounter
                    elif tile_type == 3:
                        screen.blit(event_img, (col * MAP_TILE_WIDTH, row * MAP_TILE_HEIGHT))  # Blue for event
                    elif tile_type == 4:
                        screen.blit(shop_img, (col * MAP_TILE_WIDTH, row * MAP_TILE_HEIGHT))  # Yellow for shop
                    # Draw the revealed map tile

        # Update the display
        pygame.display.flip()

    # Quit pygame properly
    pygame.quit()

