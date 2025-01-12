import pygame
import os
import numpy as np
from .board import Board
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



class Display:
    def __init__(self):
        self._ScreenWidth = SCREEN_WIDTH
        self._ScreenHeight = SCREEN_HEIGHT

        pygame.display.set_caption("Tic Tac Toe")
        self._screen = pygame.display.set_mode((self._ScreenWidth, self._ScreenHeight))

        # declaring textures
        self._Playingboard: pygame.Surface
        self._O: pygame.Surface
        self._X: pygame.Surface

        self._ButtonMultiplayer: pygame.Surface
        self._ButtonSingleplayer: pygame.Surface
        self._ButtonQuit: pygame.Surface
        self._ButtonBack: pygame.Surface

        self._ButtonRematchPlayer1: pygame.Surface
        self._ButtonRematchPlayer2: pygame.Surface
        self._ButtonRematchDraw: pygame.Surface

        self._LoadTextures()

    def _LoadTextures(self):
        """
        loading textures from assets directory
        """
        asset_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

        self._Playingboard = pygame.image.load(os.path.join(asset_dir, "board.png"))
        self._O = pygame.image.load(os.path.join(asset_dir, "O.png"))
        self._X = pygame.image.load(os.path.join(asset_dir, "X.png"))

        self._ButtonMultiplayer = pygame.image.load(os.path.join(asset_dir, "ButtonMultiplayer.png"))
        self._ButtonSingleplayer = pygame.image.load(os.path.join(asset_dir, "ButtonSingleplayer.png"))
        self._ButtonQuit = pygame.image.load(os.path.join(asset_dir, "ButtonQuit.png"))

        self._ButtonRematchPlayer1 = pygame.image.load(os.path.join(asset_dir, "ButtonRematchPlayer1.png"))
        self._ButtonRematchPlayer2 = pygame.image.load(os.path.join(asset_dir, "ButtonRematchPlayer2.png"))
        self._ButtonRematchDraw = pygame.image.load(os.path.join(asset_dir, "ButtonRematchDraw.png"))
        self._ButtonBack = pygame.image.load(os.path.join(asset_dir, "ButtonBack.png"))

    def DrawBoard(self, board: Board):
        """
        Draws the current board and position

        Args:
            board (Board): representation of the playing board as 3x3 2d numpy array
        """
        self._screen.blit(self._Playingboard, (0, 0))

        for i, row in enumerate(board):
            for j, field in enumerate(row):
                if field == "O":
                    self._screen.blit(self._O, FIELD_COORDINATES[i,j])
                elif field == "X":
                    self._screen.blit(self._X, FIELD_COORDINATES[i,j])

    def StartScreen(self):
        """
        Display the start screen
        """
        self._screen.blit(self._Playingboard, (0,0))

        self._screen.blit(self._ButtonMultiplayer, MULTI_PLAYER_POS)
        self._screen.blit(self._ButtonSingleplayer, SINGLE_PLAYER_POS)
        self._screen.blit(self._ButtonQuit, QUIT_POS)

    def EndScreen(self, winner: str = None):
        """
        display the correct end screen depending on who won

        Args:
            winner (str): a string of who won the game.

        """
        if winner == "X":
            self._screen.blit(self._ButtonRematchPlayer1, REMATCH_POS)
        elif winner == "O":
            self._screen.blit(self._ButtonRematchPlayer2, REMATCH_POS)
        elif winner is None:
            self._screen.blit(self._ButtonRematchDraw, REMATCH_POS)

        self._screen.blit(self._ButtonBack, BACK_POS)
        self._screen.blit(self._ButtonQuit, QUIT_POS)

    def ClearScreen(self):
        self._screen.blit(self._Playingboard, (0, 0))
