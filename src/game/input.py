import pygame, json, os
import numpy as np

config_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(config_path, "r") as file:
    config = json.load(file)

class Input:
    def __init__(self):
        
        self.mousePos: tuple
        self.FieldRects: np.array
        
    def ButtonCheck(self, ButtonRectangle: list):
        
        rect = pygame.rect(ButtonRectangle)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousePos = pygame.mouse.get_pos()
                if (rect.collidepoint(self.mousePos)):
                    return True
                else:
                    return False
    
    def GameInput(self):
        
        fields = config["input"]["FieldRectangles"]
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousePos = pygame.mouse.get_pos()
                for i, field in enumerate(fields):
                    column = i%3
                    row = int(i/3)
                    if field.collidepoint(self.mousePos):
                        return row, column