import pygame, json, os
import numpy as np

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")   #path to .../src/config.json

with open(config_path, "r") as file:
    config = json.load(file)


class UserInput:
    def __init__(self):

        self.mousePos: tuple
        self.FieldRects: np.array

    def ButtonCheck(self, ButtonRectangle: list, events: list):
        """
        checks if specific button was clicked

        Args:
            ButtonRectangle (list): the rectangle of the button to check [x,y,width,height]
            events (list): list of pygame events

        Returns:
            bool: was pressed or not
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
        Get inputs while game is played. determine which square was clicked

        Returns:
            tuple: row and colum that was clicked on
        """
        row: int = 0
        col: int = 0
        fields = np.array(config["input"]["FieldRectangles"])

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousePos = pygame.mouse.get_pos()
                for i, row in enumerate(fields):
                    
                    for j, field in enumerate(row):
                        rect = pygame.Rect(field)
                        if rect.collidepoint(self.mousePos):
                            return i, j
                    col+=1
                row +=1
        
