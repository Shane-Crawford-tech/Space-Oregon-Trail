import random
import pygame
import sys
import pygame_menu as pm 
from Button import Button  # Assuming you have a Button class for handling button events
from SOT import SCREEN_HEIGHT, SCREEN_WIDTH

# Constants for initial health and shields
INITIAL_HEALTH = 100
INITIAL_SHIELDS = 3  # Change initial shields to 3
PAUSE = False

# Function to start the game
def game():
    pygame.display.set_caption("SOT")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Create a surface and pass in a tuple containing its length and width
    console = pygame.Surface(((SCREEN_WIDTH/4), (3*SCREEN_HEIGHT/4)))

    # Give the surface a color to separate it from the background
    console.fill((0, 0, 0))
    rect = console.get_rect()

    # Create a surface and pass in a tuple containing its length and width
    inventory = pygame.Surface(((SCREEN_WIDTH/4), (SCREEN_HEIGHT/4)))

    # Give the surface a color to separate it from the background
    inventory.fill((50, 50, 50))
    rect = inventory.get_rect()

    # Create a surface and pass in a tuple containing its length and width
    health = pygame.Surface(((2*SCREEN_WIDTH/4), (SCREEN_HEIGHT/4)))

    # Give the surface a color to separate it from the background
    health.fill((200, 0, 0))
    rect = health.get_rect()

    # Initialize health and shields
    current_health = INITIAL_HEALTH
    current_shields = INITIAL_SHIELDS

    # Load the shield image
    shield_img = pygame.image.load("shield.png")
    shield_img = pygame.transform.scale(shield_img, (int(SCREEN_WIDTH/15), int(SCREEN_WIDTH/15)))  # Resize the image

    # Define the clickable area for the inventory button
    inventory_button_rect = pygame.Rect(0, 3 * SCREEN_HEIGHT//4, SCREEN_WIDTH//4, SCREEN_HEIGHT//4)

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is inside the inventory button area
                if event.button == 1 and inventory_button_rect.collidepoint(event.pos):
                    
                    print("Inventory button clicked!")  # Placeholder action, replace with actual action

        # Clear screen
        screen.fill((0, 0, 0))

        # Draw background
        BG = pygame.image.load("space.jpg")
        BG = pygame.transform.scale(BG, (3*SCREEN_WIDTH//4, 3*SCREEN_HEIGHT//4))
        screen.blit(BG, (0, 0))

        # Draw surfaces
        screen.blit(console, (3* SCREEN_WIDTH//4, 0))
        screen.blit(inventory, (0, 3 * SCREEN_HEIGHT//4))
        screen.blit(health, (SCREEN_WIDTH//4, 3 * SCREEN_HEIGHT//4))

        # Draw health text
        font = pygame.font.Font(None, 36)
        health_text = font.render(f"Health: {current_health}", True, (255, 255, 255))
        screen.blit(health_text, (SCREEN_WIDTH//4 + 10, 3 * SCREEN_HEIGHT//4 + 10))

        # Draw shield icons
        for i in range(current_shields):
            screen.blit(shield_img, (SCREEN_WIDTH//2.8 + i * SCREEN_WIDTH/10, 3 * SCREEN_HEIGHT//4 + 50))  # Adjust the position of shield icons

        pygame.display.flip()

game()
