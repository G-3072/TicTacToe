import pygame, json, os
import numpy as np

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")   #path to .../src/config.json

with open(config_path, "r") as file:
    config = json.load(file)


class Input:
    def __init__(self):

        self.mousePos: tuple
        self.FieldRects: np.array

    def ButtonCheck(self, ButtonRectangle: list):
        """
        chacks if specific button was clicked

        Args:
            ButtonRectangle (list): the rectangle of the button to check [x,y,width,height]

        Returns:
            bool: was pressed or not
        """
        rect = pygame.rect(ButtonRectangle)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousePos = pygame.mouse.get_pos()
                if rect.collidepoint(self.mousePos):
                    return True
                else:
                    return False

    def GameInput(self):
        """
        Get inputs while game is played. determine which square was clicked

        Returns:
            tuple: row and colum that was clicked on
        """
        row, col = 0
        fields = np.array(config["input"]["FieldRectangles"])

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousePos = pygame.mouse.get_pos()
                for i, row in enumerate(fields):
                    
                    for j, field in enumerate(row):
                    
                        if field.collidepoint(self.mousePos):
                            return row, col
                    col+=1
                row +=1
