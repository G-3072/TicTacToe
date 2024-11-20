import pygame
from .config import FIELD_RECTANGLES


class PlayerInput:
    
    def __init__(self):
        self.mousePos: list

    def ButtonCheck(self, ButtonRectangle: list, events: list):
        """
        Checks if a specific button was clicked.

        Args:
            ButtonRectangle (list): The rectangle of the button to check [x,y,width,height].
            events (list): List of pygame events.

        Returns:
            bool: Was pressed or not.
        """
        rect = pygame.Rect(ButtonRectangle)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousePos = pygame.mouse.get_pos()
                if rect.collidepoint(self.mousePos):
                    return True
        return False

    def GameInput(self, events: list):
        """
        Get inputs while the game is played. Determine which square was clicked.

        Returns:
            tuple: Row and column that was clicked on.
        """

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousePos = pygame.mouse.get_pos()

                for i, row in enumerate(FIELD_RECTANGLES):

                    for j, square in enumerate(row):
                        rect = pygame.Rect(square)
                        if rect.collidepoint(self.mousePos):
                            return i, j
