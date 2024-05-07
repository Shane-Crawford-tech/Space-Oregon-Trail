import pygame

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