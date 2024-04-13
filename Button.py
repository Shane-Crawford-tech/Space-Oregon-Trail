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
            self.image = self.image.render(self.image_input, True, (self.image))
        else:
            self.text = self.font.render(self.text_input, True, (255, 255, 255))
