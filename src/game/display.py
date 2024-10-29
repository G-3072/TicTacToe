import pygame
import numpy as np

class display:
    def __init__(self):
        self.ScreenWidth = 920  #920 width/heigth bc 3*300 square + 2 * 10 line
        self.ScreenHeigth = 920

        self.screen = pygame.display.set_mode((self.ScreenWidth, self.ScreenHeigth))
        
        self.board = pygame.image.load("")

    def DrawBoard(self):
        pass
    
    def UpdateScreen(self, board: np.array):
        pass

    def ClearScreen(self):
        pass
    
    