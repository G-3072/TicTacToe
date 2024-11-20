import pygame
import os
import numpy as np
from .config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FIELD_COORDINATES,
    MULTI_PLAYER_POS,
    SINGLE_PLAYER_POS,
    QUIT_POS,
    REMATCH_POS,
    BACK_POS,
)
from .board import Board


class Display:
    def __init__(self):
        self.ScreenWidth = SCREEN_WIDTH
        self.ScreenHeight = SCREEN_HEIGHT

        pygame.display.set_caption("Tic Tac Toe")
        self.screen = pygame.display.set_mode((self.ScreenWidth, self.ScreenHeight))

        # declaring textures
        self.Playingboard: pygame.Surface
        self.O: pygame.Surface
        self.X: pygame.Surface

        self.ButtonMultiplayer: pygame.Surface
        self.ButtonSingleplayer: pygame.Surface
        self.ButtonQuit: pygame.Surface
        self.ButtonBack: pygame.Surface

        self.ButtonRematchPlayer1: pygame.Surface
        self.ButtonRematchPlayer2: pygame.Surface
        self.ButtonRematchDraw: pygame.Surface

        self.__LoadTextures__()

    def __LoadTextures__(self):
        """
        loading textures from assets directory
        """
        asset_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

        self.Playingboard = pygame.image.load(os.path.join(asset_dir, "board.png"))
        self.O = pygame.image.load(os.path.join(asset_dir, "O.png"))
        self.X = pygame.image.load(os.path.join(asset_dir, "X.png"))

        self.ButtonMultiplayer = pygame.image.load(
            os.path.join(asset_dir, "ButtonMultiplayer.png")
        )
        self.ButtonSingleplayer = pygame.image.load(
            os.path.join(asset_dir, "ButtonSingleplayer.png")
        )
        self.ButtonQuit = pygame.image.load(os.path.join(asset_dir, "ButtonQuit.png"))

        self.ButtonRematchPlayer1 = pygame.image.load(
            os.path.join(asset_dir, "ButtonRematchPlayer1.png")
        )
        self.ButtonRematchPlayer2 = pygame.image.load(
            os.path.join(asset_dir, "ButtonRematchPlayer2.png")
        )
        self.ButtonRematchDraw = pygame.image.load(
            os.path.join(asset_dir, "ButtonRematchDraw.png")
        )
        self.ButtonBack = pygame.image.load(os.path.join(asset_dir, "ButtonBack.png"))

    def DrawBoard(self, board: Board):
        """
        Draws the current board and position

        Args:
            board (np.array): representation of the playing board as 3x3 2d numpy array
        """
        self.screen.blit(self.Playingboard, (0, 0))

        for i, row in enumerate(board):
            for j, field in enumerate(row):
                if field == "O":
                    self.screen.blit(self.O, FIELD_COORDINATES[i,j])
                elif field == "X":
                    self.screen.blit(self.X, FIELD_COORDINATES[i,j])

    def StartScreen(self):
        """
        Display the start screen
        """
        self.screen.blit(self.Playingboard, (0,0))

        self.screen.blit(self.ButtonMultiplayer, MULTI_PLAYER_POS)
        self.screen.blit(self.ButtonSingleplayer, SINGLE_PLAYER_POS)
        self.screen.blit(self.ButtonQuit, QUIT_POS)

    def EndScreen(self, winner: str):
        """
        display the correct end screen depending on who won

        Args:
            winner (str): a string of who won the game.

        """
        if winner == "X":
            self.screen.blit(self.ButtonRematchPlayer1, REMATCH_POS)
        elif winner == "O":
            self.screen.blit(self.ButtonRematchPlayer2, REMATCH_POS)
        elif winner == "draw":
            self.screen.blit(self.ButtonRematchDraw, REMATCH_POS)

        self.screen.blit(self.ButtonBack, BACK_POS)
        self.screen.blit(self.ButtonQuit, QUIT_POS)

    def ClearScreen(self):
        self.screen.blit(self.Playingboard, (0, 0))
