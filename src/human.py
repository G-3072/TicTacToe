import pygame
from src import FIELD_RECTANGLES, Player

class Human(Player):
    def __init__(self, symbol: str):
        self.symbol = symbol
        
    def getSymbol(self):
        return self.symbol
    
    def getMove(self, events: list):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousePos = pygame.mouse.get_pos()

                for i, row in enumerate(FIELD_RECTANGLES):

                    for j, square in enumerate(row):
                        rect = pygame.Rect(square)
                        if rect.collidepoint(self.mousePos):
                            return i, j
    
    def CheckButtonClick(self, ButtonRectangle: list, events: list):
        rect = pygame.Rect(ButtonRectangle)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousePos = pygame.mouse.get_pos()
                if rect.collidepoint(self.mousePos):
                    return True
        return False
