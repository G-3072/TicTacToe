from abc import ABC, abstractmethod
import pygame
from .config import FIELD_RECTANGLES

class Player(ABC):
    _symbol: str
    @abstractmethod
    def getSymbol(self):
        pass
    
    @abstractmethod
    def getMove(self):
        pass

class Human(Player):
    def __init__(self, symbol: str):
        self._symbol = symbol
        
    def getSymbol(self):
        return self._symbol
    
    def getMove(self, events: list = None):
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

