import pygame
import numpy as np
import os

class display:
    def __init__(self):
        self.ScreenWidth = 920  #920 width/heigth bc 3*300 square + 2 * 10 line
        self.ScreenHeigth = 920

        self.screen = pygame.display.set_mode((self.ScreenWidth, self.ScreenHeigth))
        
        #declaring textures
        self.board: pygame.Surface
        self.O: pygame.Surface
        self.X: pygame.Surface
        
        self.ButtonMultiplayer: pygame.Surface
        self.ButtonSingleplayer: pygame.Surface
        self.ButtonQuit: pygame.Surface
        
        self.ButtonRematchPlayer1: pygame.Surface
        self.ButtonRematchPlayer2: pygame.Surface
        self.ButtonRematchDraw: pygame.Surface
        
    
    def _LoadTextures(self):
        """
        loading textures from assets directory
        """
        asset_dir = os.path.join(os.path.dirname(__file__), "assets")
        
        self.board = pygame.image.load(os.path.join(asset_dir, "board.png"))
        self.O = pygame.image.load(os.path.join(asset_dir, "O.png"))
        self.X = pygame.image.load(os.path.join(asset_dir, "X.png"))
        
        self.ButtonMultiplayer = pygame.image.load(os.path.join(asset_dir, "ButtonMultiplayer.png"))
        self.ButtonSingleplayer = pygame.image.load(os.path.join(asset_dir, "ButtonSingleplayer.png"))
        self.ButtonQuit = pygame.image.load(os.path.join(asset_dir, "ButtonQuit.png"))
        
        self.ButtonRematchPlayer1 = pygame.image.load(os.path.join(asset_dir, "ButtonRematchPlayer1.png"))
        self.ButtonRematchPlayer2 = pygame.image.load(os.path.join(asset_dir, "ButtonRematchPlayer2.png"))
        self.ButtonRematchDraw = pygame.image.load(os.path.join(asset_dir, "ButtonRematchDraw.png"))
        

        
        
        
        
        
        
        

    def DrawBoard(self):
        pass
    
    def UpdateScreen(self, board: np.array):
        pass

    def ClearScreen(self):
        pass
    
    