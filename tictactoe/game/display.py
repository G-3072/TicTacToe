import pygame, os, json
import numpy as np

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")   #path to .../src/config.json

with open(config_path, "r") as file:
    config = json.load(file)


class Display:
    def __init__(self):
        self.ScreenWidth = config["display"]["ScreenWidth"]
        self.ScreenHeight = config["display"]["ScreenHeight"]

        pygame.display.set_caption("Tic Tac Toe")
        self.screen = pygame.display.set_mode((self.ScreenWidth, self.ScreenHeight))

        # declaring textures
        self.Playingboard: pygame.Surface
        self.O: pygame.Surface
        self.X: pygame.Surface

        self.ButtonMultiplayer: pygame.Surface
        self.ButtonSingleplayer: pygame.Surface
        self.ButtonQuit: pygame.Surface

        self.ButtonRematchPlayer1: pygame.Surface
        self.ButtonRematchPlayer2: pygame.Surface
        self.ButtonRematchDraw: pygame.Surface

        self.FieldCoordinates = np.array(config["display"]["FieldCoordinates"])

    def LoadTextures(self):
        """
        loading textures from assets directory
        """
        asset_dir = os.path.join(os.path.dirname(__file__), "assets")

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
        print("textures Loaded")

    def DrawBoard(self, board: np.array = [["", "", ""], ["", "", ""], ["", "", ""]]):
        """
        Draws the current board and position

        Args:
            board (np.array): representation of the playing board as 3x3 2d numpy array
        """
        self.screen.blit(self.Playingboard, (0, 0))

        for i, row in enumerate(board):
            for j, field in enumerate(board[i]):
                if field == "O":
                    self.screen.blit(self.O, self.FieldCoordinates[i][j])
                elif field == "X":
                    self.screen.blit(self.X, self.FieldCoordinates[i][j])

    def StartScreen(self):
        """
        Display the start screen
        """
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.ButtonMultiplayer, config["display"]["MultiPlayerPos"])
        self.screen.blit(self.ButtonSingleplayer, config["display"]["SinglePlayerPos"])
        self.screen.blit(self.ButtonQuit, config["display"]["QuitPos"])

    def EndScreen(self, winner: str = ""):
        """
        display the correct endScreen depending on who won

        Args:
            winner (str, optional): a string of who won the game. empty string means draw.
            Defaults to "".
        """
        if winner == "player1":
            self.screen.blit(self.ButtonRematchPlayer1, config["display"]["RematchPos"])
        elif winner == "player2":
            self.screen.blit(self.ButtonRematchPlayer2, config["display"]["RematchPos"])
        elif winner == "":
            self.screen.blit(self.ButtonRematchDraw, config["display"]["RematchPos"])

        self.screen.blit(self.ButtonQuit, config["display"]["QuitPos"])

    def ClearScreen(self):
        self.screen.blit(self.Playingboard, (0, 0))
